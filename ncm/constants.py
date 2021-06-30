# -*- coding: utf-8 -*-
import random
import string

# Encrypt key
modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
nonce = '0CoJUm6Qyw8W8jud'
pub_key = '010001'


headers = {
    'Accept': '*/*',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Referer': 'http://music.163.com',
    'Cookie': 'appver=2.0.2; _ntes_nuid={};'.format(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32)))
}
song_download_url = 'http://music.163.com/weapi/song/enhance/player/url?csrf_token='


def get_song_url(song_id):
    return 'http://music.163.com/api/song/detail/?ids=[{}]'.format(song_id)


def get_album_url(album_id):
    return 'http://music.163.com/api/album/{}/'.format(album_id)


def get_artist_url(artist_id):
    return 'http://music.163.com/api/artist/{}'.format(artist_id)


def get_playlist_url(playlist_id):
    return 'http://music.163.com/api/v6/playlist/detail?id={}'.format(playlist_id)
