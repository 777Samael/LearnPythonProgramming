from id3_types import id3_field_encodings, apic_picture_types, frame_types
from os import SEEK_CUR, path
from typing import BinaryIO

filename = 'Someday.mp3'


def decode_size(encoded_size: bytes) -> int:
    """Decode and return an ID3 encoded size as a positive integer.

    The ID3v2 tag size is encoded with four bytes, where the
    most significant bit (bit 7) is set to zero in every byte.
    This gives a total of 28 bits. The zeroed high bit is ignored.
    Each byte after the least significant is shifted left 7 places.
    Thus:
        byte 3 is shifted left 21 places.

        byte 2 is shifted left 14 places

        byte 1 is shifted left 7 places

        byte 0 is unchanged,

        Or-ing the 4 bytes gives the decoded size.

    For example, a size of 257 bytes is represented as $00 00 02 01.
    Ignoring the 2 most significant bytes for simplicity
    (because they're zero):

                    0000 0010  ($02) << 7 =
          0000 0001 0000 0000 |
                    0000 0001
          -------------------
          0000 0001 0000 0001 ($01 01, 257 in decimal)

    :param encoded_size: The 4 bytes making up the encoded size.
    :return: The decoded size, as an integer.
    """
    return encoded_size[0] << 21 \
           | encoded_size[1] << 14 \
           | encoded_size[2] << 7 \
           | encoded_size[3]


def read_c_string(binary_file: BinaryIO, c_str_encoding: str) -> str:
    """
    Read a null-terminated sequence of bytes,
    and decode it to a unicode string.

    Note: This function will probably crash if the file pointer
    isn't positioned on the first character of a c-string
    (it's fine for the terminating $00 of an empty string).

    :param binary_file: The file to read from. Must be opened in binary mode,
        and the file pointer should be positioned at the correct point
        to start reading from.
    :param c_str_encoding: The encoding to use when decoding the bytes.
    :return: A Python str corresponding to the decoded c-string.
    :raises UnicodeDecodeError: This could be raised if the file pointer
        isn't positioned at the start of a valid Unicode sequence. You
        may get an exception, or the returned string could be unintelligible.
    """
    byte_array = bytearray()
    # Python has no built-in way to read c-strings,
    # read character by character till we encounter 0.
    byte_read = binary_file.read(1)
    while byte_read and byte_read != b'\x00':
        byte_array += byte_read
        byte_read = binary_file.read(1)

    if byte_array != b'\x00':
        return byte_array.decode(c_str_encoding)
    else:
        return ''


with open(filename, 'rb') as mp3_file:
    header = mp3_file.read(10)

    # Do we have an ID3 tag?
    if header[:5] == b'ID3\x03\x00':
        # Flags
        print(f'Flags: {header[5]:#010b}')
        # Calculate the size
        size_bytes = header[-4:]
        size = decode_size(size_bytes)
        print(f'Tag size: {size} bytes')

        # Skip extended header, if there is one
        if header[5] & 0b01000000:
            # Extended header present. The 4 byte encoded size
            # follows immediately after the 10 byte file header.
            ext_size = decode_size(mp3_file.read(4))
            print(f'Extended header, size is {ext_size} bytes.')

            # We're not interested in the extended header, seek past it.
            mp3_file.seek(ext_size, SEEK_CUR)

        while True:
            print('*' * 80)
            print(f'Current file position: {mp3_file.tell()}')
            # read 10 byte frame header
            frame_header = mp3_file.read(10)
            frame_id = frame_header[:4]

            if frame_id in frame_types:
                print(f'Found frame type: {frame_id}')

                # We need the frame size.
                frame_size = int.from_bytes(frame_header[4:8], 'big')
                print(f'Frame size: {frame_size}')

                # Only process text, WXXX and APIC frames
                if frame_id.startswith(b'T'):  # a text field
                    # Get the encoding byte.
                    encoding_byte = mp3_file.read(1)[0]
                    encoding = id3_field_encodings[encoding_byte]
                    print(f'encoding is {encoding}')

                    # Now read & decode the data. We've already read byte 0,
                    # so there are `size - 1` bytes left.
                    text = mp3_file.read(frame_size - 1).decode(encoding)
                    print(f'{frame_types[frame_id]}: {text}')

                elif frame_id == b'WXXX':
                    # Get the encoding byte.
                    encoding_byte = mp3_file.read(1)[0]
                    encoding = id3_field_encodings[encoding_byte]
                    print(f'encoding is {encoding}')

                    # Now read and decode the data.
                    # Note: we've already read 1 byte of the frame.
                    description_and_url = mp3_file.read(frame_size - 1)

                    # Split on 00 byte to get the 2 parts
                    parts = description_and_url.split(b'\x00')
                    description = parts[0].decode(encoding)
                    url = parts[-1].decode('iso-8859-1')
                    print(f'{frame_types[frame_id]}:')
                    print(f'\tDescription: {description}')
                    print(f'\tURL: {url}')

                elif frame_id == b'APIC':
                    frame_data_start = mp3_file.tell()
                    print(f'APIC frame starts at {frame_data_start}')

                    # Get the encoding byte.
                    encoding_byte = mp3_file.read(1)[0]
                    encoding = id3_field_encodings[encoding_byte]
                    print(f'APIC text encoding: {encoding}')

                    # Next we have a null-terminated string.
                    mime_type = read_c_string(mp3_file, 'iso-8859-1')
                    if mime_type == '':
                        mime_type = 'image/'
                    print(f'Mime type: {mime_type}')

                    # read 1 byte picture type
                    picture_type = int.from_bytes(mp3_file.read(1), 'big')
                    apic_picture_name = apic_picture_types[picture_type]
                    print(f'Found {apic_picture_name} image')

                    # Description is also a null-terminated string
                    description = read_c_string(mp3_file, encoding)
                    print(f'Image description: { description}')

                    # Now write the image to a new file.
                    if mime_type.startswith('image/'):
                        image_data_start = mp3_file.tell()
                        print(f'Image data starts at {image_data_start}')
                        image_size = frame_size - (image_data_start - frame_data_start)
                        print(f'Image size = {image_size}')
                        image_data = mp3_file.read(image_size)

                        image_type = mime_type.split('/')[-1]

                        # get filename only
                        base_filename = path.split(filename)[1]

                        # now remove extension
                        base_filename = path.splitext(base_filename)[0]

                        picture_filename = f'{base_filename}_{apic_picture_name}.{image_type}'
                        print(f'Writing image file {picture_filename}')

                        with open(picture_filename, 'wb') as output_file:
                            output_file.write(image_data)

                else:
                    # Found a frame that we're not going to process.
                    # Skip it by seeking forward `frame_size` bytes
                    mp3_file.seek(frame_size, SEEK_CUR)
                    # Now skip any zero bytes
                    next_byte = mp3_file.read(1)
                    # Check for an empty bytearray, to avoid attempting to read past EOF (end of file).
                    while next_byte and next_byte == b'\0':
                        next_byte = mp3_file.read(1)
                    # If we've just read a non-zero byte, it will be part of the next frame.
                    # Move the file pointer back 1 byte, to read it again next time round.
                    if next_byte != b'':
                        mp3_file.seek(-1, SEEK_CUR)
                print(f'seek position after frame: {mp3_file.tell()}')
            else:
                # Found an unrecognised frame (or we've exhausted all frames)
                break
