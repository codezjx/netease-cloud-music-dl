# -*- coding: utf-8 -*-

from mutagen.mp3 import MP3, HeaderNotFoundError
from mutagen.id3 import ID3, APIC, TPE1, TIT2, TALB, TCON, USLT, SYLT, error
import time,datetime,re

def add_metadata_to_song(file_path, cover_path, song, gener, lyric):
    # If no ID3 tags in mp3 file
    try:
        audio = MP3(file_path, ID3=ID3)
    except HeaderNotFoundError:
        print('Can\'t sync to MPEG frame, not an validate MP3 file!')
        return

    if audio.tags is None:
        print('No ID3 tag, trying to add one!')
        try:
            audio.add_tags()
            audio.save()
        except error as e:
            print('Error occur when add tags:', str(e))
            return

    # Modify ID3 tags
    id3 = ID3(file_path)
    # Remove old 'APIC' frame
    # Because two 'APIC' may exist together with the different description
    # For more information visit: http://mutagen.readthedocs.io/en/latest/user/id3.html
    if id3.getall('APIC'):
        id3.delall('APIC')
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
    # add genre
    id3.add(
        TCON(
            encoding=3,
            text=gener
        )
    )
    # add Unsychronised lyric
    id3.add(
        USLT(
            encoding=3,
            lang='chs',
            desc="Unsychronised lyric",
            text=lyric
        )
    )
    # add Synchronized lyric
    sync_lyric = []
    for line in lyric.split("\n"):
        #print(line)
        if line.find("]") != -1:
            time_str = line.split("]")[0].replace("[","")
            lyric_str = line.split("]")[1]
            try:
                time_array = re.findall(r"\d+:\d+\.\d+", time_str)
                if len(time_array) == 1:
                    time_m = int(time_array[0].split(":")[0])
                    time_s = int(time_array[0].split(":")[1].split(".")[0])
                    time_ms = int(time_array[0].split(":")[1].split(".")[1])
                    sync_lyric.append((lyric_str,time_m*60*1000+time_s*1000+time_ms))
            except:
                print(time_str)

    id3.add(
        SYLT(
            encoding=3,
            lang='chs',
            format=2,
            type=1,
            desc="Synchronized lyric",
            text=sync_lyric
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
