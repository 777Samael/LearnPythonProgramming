import os
import fnmatch
import id3reader_p3 as id3reader


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, f"*{extension}"):
            absolute_path = os.path.abspath(path)  # create absolute path
            yield os.path.join(absolute_path, file)  # ise absolute_path in yielded values


my_music = find_music('d:\\Muzyka', 'mp3')

error_list = []

for f in my_music:
    try:
        id3r = id3reader.Reader(f)
        print(f"Artist: {id3r.get_value('performer')}, Album: {id3r.get_value('album')}, Track: {id3r.get_value('track')},"
              f" Song: {id3r.get_value('title')}")
    except:
        error_list.append(f)

for error_file in error_list:
    print(error_file)


# for root, dirnames, fnames in os.walk('d:\\Muzyka'):
#     print("I am looking in", root)
#     print("These are the subdirectories:")
#     for dirname in dirnames:
#         print(os.path.join(root, dirname))
#
#     print("These are the filenames:")
#     for fname in fnames:
#         print(os.path.join(root, fname))
