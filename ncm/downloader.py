# -*- coding: utf-8 -*-

import os
import requests

from ncm.api import CloudApi
from ncm.file_util import add_metadata_to_song


def download_song_by_id(song_id, download_folder):
    # get song info
    api = CloudApi()
    song = api.get_song(song_id)
    download_song_by_song(song, download_folder)


def download_song_by_song(song, download_folder):
    # get song info
    api = CloudApi()
    song_id = song['id']
    song_name = song['name']
    artist_name = song['artists'][0]['name']
    song_file_name = '{}_{}.mp3'.format(artist_name, song_name)

    # download song
    song_url = api.get_song_url(song_id)
    is_already_download = download_file(song_url, song_file_name, download_folder)
    if is_already_download:
        print('Mp3 file already download:', song_file_name)
        return

    # download cover
    cover_url = song['album']['blurPicUrl']
    cover_file_name = 'cover_{}.jpg'.format(song_id)
    download_file(cover_url, cover_file_name, download_folder)

    # add metadata for song
    song_file_path = os.path.join(download_folder, song_file_name)
    cover_file_path = os.path.join(download_folder, cover_file_name)
    add_metadata_to_song(song_file_path, cover_file_path, song)

    # delete cover file
    os.remove(cover_file_path)


def download_file(file_url, file_name, folder):

    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, file_name)

    response = requests.get(file_url, stream=True)
    length = int(response.headers.get('Content-Length'))

    # TODO need to improve whether the file exists
    if os.path.exists(file_path) and os.path.getsize(file_path) > length:
        return True

    progress = ProgressBar(file_name, length)

    with open(file_path, 'wb') as file:
        for buffer in response.iter_content(chunk_size=1024):
            if buffer:
                file.write(buffer)
                progress.refresh(len(buffer))
    return False


class ProgressBar(object):

    def __init__(self, file_name, total):
        super().__init__()
        self.file_name = file_name
        self.count = 0
        self.prev_count = 0
        self.total = total
        self.status = 'Downloading:'
        self.end_str = '\r'

    def __get_info(self):
        return '[{}] {:.2f}KB, Progress: {:.2f}%'\
            .format(self.file_name, self.total/1024, self.count/self.total*100)

    def refresh(self, count):
        self.count += count
        # Update progress if down size > 10k
        if (self.count - self.prev_count) > 10240:
            self.prev_count = self.count
            print(self.__get_info(), end=self.end_str)
        # Finish downloading
        if self.count >= self.total:
            self.status = 'Downloaded:'
            self.end_str = '\n'
            print(self.__get_info(), end=self.end_str)
