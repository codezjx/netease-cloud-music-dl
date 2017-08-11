# -*- coding: utf-8 -*-
import os

from configparser import ConfigParser

# Config key
_CONFIG_KEY_DOWNLOAD_HOT_MAX = 'download.hot_max'
_CONFIG_KEY_DOWNLOAD_DIR = 'download.dir'
_CONFIG_KEY_SONG_NAME_TYPE = 'song.name_type'
_CONFIG_KEY_SONG_FOLDER_TYPE = 'song.folder_type'

# Base path
_CONFIG_MAIN_PATH = os.path.join(os.path.expanduser('~'), '.ncm')
_CONFIG_FILE_PATH = os.path.join(_CONFIG_MAIN_PATH, 'ncm.ini')
_DEFAULT_DOWNLOAD_PATH = os.path.join(_CONFIG_MAIN_PATH, 'download')

# Global config value
DOWNLOAD_HOT_MAX_DEFAULT = 50
DOWNLOAD_HOT_MAX = DOWNLOAD_HOT_MAX_DEFAULT
DOWNLOAD_DIR = ''
SONG_NAME_TYPE = 1
SONG_FOLDER_TYPE = 1


def load_config():
    if not os.path.exists(_CONFIG_FILE_PATH):
        init_config_file()

    cfg = ConfigParser()
    cfg.read(_CONFIG_FILE_PATH)

    global DOWNLOAD_HOT_MAX
    global DOWNLOAD_DIR
    global SONG_NAME_TYPE
    global SONG_FOLDER_TYPE

    DOWNLOAD_HOT_MAX = cfg.getint('settings', _CONFIG_KEY_DOWNLOAD_HOT_MAX)
    DOWNLOAD_DIR = cfg.get('settings', _CONFIG_KEY_DOWNLOAD_DIR)
    SONG_NAME_TYPE = cfg.getint('settings', _CONFIG_KEY_SONG_NAME_TYPE)
    SONG_FOLDER_TYPE = cfg.getint('settings', _CONFIG_KEY_SONG_FOLDER_TYPE)


def init_config_file():
    default_config = '''\
    [settings]
    
    #--------------------------------------
    # Max download hot song numbers
    # 
    # Range: 0 < hot_max < 50
    #--------------------------------------
    {key_max} = {value_max}
    
    #--------------------------------------
    # Song download directory
    #--------------------------------------
    {key_dir} = {value_dir}
    
    #--------------------------------------
    # Song name type, maybe one of the 
    # following values:
    #
    # 1: song_name.mp3
    # 2: artist_name - song_name.mp3
    # 3: song_name - artist_name.mp3
    #--------------------------------------
    {key_name_type} = 1
    
    #--------------------------------------
    # Song folder type, maybe one of the 
    # following values:
    #
    # 1: download.dir
    # 2: download.dir/artist_name
    # 3: download.dir/artist_name/album_name
    #--------------------------------------
    {key_folder_type} = 1
    '''.format(key_max=_CONFIG_KEY_DOWNLOAD_HOT_MAX,
               value_max=DOWNLOAD_HOT_MAX_DEFAULT,
               key_dir=_CONFIG_KEY_DOWNLOAD_DIR,
               value_dir=_DEFAULT_DOWNLOAD_PATH,
               key_name_type=_CONFIG_KEY_SONG_NAME_TYPE,
               key_folder_type=_CONFIG_KEY_SONG_FOLDER_TYPE)

    if not os.path.exists(_CONFIG_MAIN_PATH):
        os.makedirs(_CONFIG_MAIN_PATH)
    f = open(_CONFIG_FILE_PATH, 'w')
    f.write(default_config)
    f.close()
