# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='netease-cloud-music-dl',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.17.3',
        'pycrypto>=2.6.1',
        'mutagen>=1.38.0',
    ],

    entry_points={
        'console_scripts': [
            'ncm = ncm.start:main',
        ]
    },

    license='Apache License V2',
    author='codezjx',
    author_email='code.zjx@gmail.com',
    url='https://github.com/codezjx/netease-cloud-music-dl',
    description='Netease cloud music downloader, with full ID3 metadata!',
    keywords=['ncm', 'cloud-music', 'downloader'],
)