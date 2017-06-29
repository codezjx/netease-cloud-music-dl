# -*- coding: utf-8 -*-

from mutagen.id3 import ID3, APIC, TPE1, TIT2, TALB


def add_metadata_to_song(file_path, cover_path, song):
    id3 = ID3(file_path)
    # add album cover
    id3.add(
        APIC(
            encoding=0,         # 3 is for UTF8, but here we use 0 (LATIN1) for 163, orz~~~
            mime='image/jpeg',  # image/jpeg or image/png
            type=3,             # 3 is for the cover(front) image
            data=open(cover_path, 'rb').read()
        )
    )
    # add artist name
    id3.add(
        TPE1(
            encoding=3,
            text=song['artists'][0]['name']
        )
    )
    # add song name
    id3.add(
        TIT2(
            encoding=3,
            text=song['name']
        )
    )
    # add album name
    id3.add(
        TALB(
            encoding=3,
            text=song['album']['name']
        )
    )
    id3.save(v2_version=3)
