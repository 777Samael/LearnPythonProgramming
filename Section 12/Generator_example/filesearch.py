import os
import fnmatch


def find_albums(root, artist_name):
    caps_name = artist_name.upper()   # 2, 3
    for path, directories, files in os.walk(root):
        # for artist in fnmatch.filter(directories, artist_name):   # 1
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):    # 2
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):    # 3
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):    # we want the path, not the name of the album
            yield song


album_list = find_albums("music", "black*")
song_list = find_songs(album_list)

# for a in album_list:
#     print(a)

for s in song_list:
    print(s)
