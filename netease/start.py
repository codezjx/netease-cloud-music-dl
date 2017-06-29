# -*- coding: utf-8 -*-
import argparse
import os
import config

from api import CloudApi
from downloader import download_song_by_id
from downloader import download_song_by_song

# load the config first
config.load_config()
print('max:', config.DOWNLOAD_HOT_MAX)
print('dir:', config.DOWNLOAD_DIR)
print('name_type:', config.SONG_NAME_TYPE)
print('folder_type:', config.SONG_FOLDER_TYPE)


parser = argparse.ArgumentParser(description='Welcome to netease cloud music downloader!')
parser.add_argument('-s', metavar='song_id', dest='song_id',
                    help='Download a song by song_id')
parser.add_argument('-ss', metavar='song_ids', dest='song_ids', nargs='+',
                    help='Download a song list, song_id split by space')
parser.add_argument('-hot', metavar='artist_id', dest='artist_id',
                    help='Download an artist hot 50 songs by artist_id')
parser.add_argument('-a', metavar='album_id', dest='album_id',
                    help='Download an album all songs by album_id')
parser.add_argument('-p', metavar='playlist_id', dest='playlist_id',
                    help='Download a playlist all songs by playlist_id')
args = parser.parse_args()
api = CloudApi()


def download_hot_songs(artist_id):
    songs = api.get_hot_songs(artist_id)
    folder_name = songs[0]['artists'][0]['name'] + '_hot50'
    folder_path = os.path.join(config.DOWNLOAD_DIR, folder_name)
    for i, song in enumerate(songs):
        print(str(i + 1) + ' song name:' + song['name'])
        download_song_by_song(song, folder_path)


def download_album_songs(album_id):
    songs = api.get_album_songs(album_id)
    folder_name = songs[0]['artists'][0]['name'] + '_' + songs[0]['album']['name']
    folder_path = os.path.join(config.DOWNLOAD_DIR, folder_name)
    for i, song in enumerate(songs):
        print(str(i + 1) + ' song name:' + song['name'])
        download_song_by_song(song, folder_path)


def download_playlist_songs(playlist_id):
    songs, playlist_name = api.get_playlist_songs(playlist_id)
    folder_name = 'playlist_' + playlist_name
    folder_path = os.path.join(config.DOWNLOAD_DIR, folder_name)
    for i, song in enumerate(songs):
        print(str(i + 1) + ' song name:' + song['name'])
        download_song_by_song(song, folder_path)


if args.song_id:
    download_song_by_id(args.song_id, config.DOWNLOAD_DIR)
elif args.song_ids:
    for song_id in args.song_ids:
        download_song_by_id(song_id, config.DOWNLOAD_DIR)
elif args.artist_id:
    download_hot_songs(args.artist_id)
elif args.album_id:
    download_album_songs(args.album_id)
elif args.playlist_id:
    download_playlist_songs(args.playlist_id)


# song = api.get_song('464035731')
# print('song id:{}, song name:{}, album:{}'.format(song['id'], song['name'], song['album']['name']))

# from mutagen.mp3 import MP3
# from mutagen.id3 import ID3, APIC, error
#
#
# file_path = '/Users/codezjx/Downloads/test.mp3'
# cover_path = '/Users/codezjx/Downloads/test.jpg'
#
# audio = MP3(file_path, ID3=ID3)
# if audio.tags is None:
#     print('No ID3 tag, try to add one!')
#     try:
#         audio.add_tags()
#     except error:
#         pass
# audio.tags.add(
#     APIC(
#         encoding=3,        # 3 is for utf-8
#         mime='image/jpg',  # image/jpeg or image/png
#         type=3,            # 3 is for the cover(front) image
#         data=open(cover_path, 'rb').read()
#     )
# )
# audio.save()
