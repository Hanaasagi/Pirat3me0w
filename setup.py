# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
from src import __version__, __author__, __email__

setup(
    name='Pirat3me0w',
    version=__version__,
    author=__author__,
    author_email=__email__,
    keywords='Downloader, nhentai.net',
    description='Download manga from nhentai.net',
    url='https://github.com/Hanaasagi/Pirat3me0w',
    packages=['src', 'src.logutils'],
    entry_points={
        'console_scripts': ['piratemeow = src.command:main']
    },
    license='MIT',
)
