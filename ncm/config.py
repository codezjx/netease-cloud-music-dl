# -*- coding: utf-8 -*-
import os

from configparser import ConfigParser

# Config key
_CONFIG_KEY_DOWNLOAD_HOT_MAX = 'download.hot_max'
_CONFIG_KEY_DOWNLOAD_DIR = 'download.dir'
_CONFIG_KEY_SONG_NAME_TYPE = 'song.name_type'
_CONFIG_KEY_SONG_FOLDER_TYPE = 'song.folder_type'

# Base path
_CONFIG_MAIN_PATH = os.path.join(os.getenv('HOME'), '.ncm')
_CONFIG_FILE_PATH = os.path.join(_CONFIG_MAIN_PATH, 'ncm.ini')
_DEFAULT_DOWNLOAD_PATH = os.path.join(_CONFIG_MAIN_PATH, 'download')

# Global config value
DOWNLOAD_HOT_MAX = 50
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
    {key_max} = 50
    {key_dir} = {value_dir}
    {key_name_type} = 1
    {key_folder_type} = 1
    '''.format(key_max=_CONFIG_KEY_DOWNLOAD_HOT_MAX,
               key_dir=_CONFIG_KEY_DOWNLOAD_DIR,
               value_dir=_DEFAULT_DOWNLOAD_PATH,
               key_name_type=_CONFIG_KEY_SONG_NAME_TYPE,
               key_folder_type=_CONFIG_KEY_SONG_FOLDER_TYPE)

    if not os.path.exists(_CONFIG_MAIN_PATH):
        os.makedirs(_CONFIG_MAIN_PATH)
    f = open(_CONFIG_FILE_PATH, 'w')
    f.write(default_config)
    f.close()
