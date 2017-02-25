#!/usr/bin/env python2.7
# -*- coding:UTF-8 -*-

from cmd_parser import cmd_parser
from parser import nhentai_parser
from nhentai import nhentai
from downloader import Downloader
from watcher import Watcher


def main():
    args = cmd_parser()

    task_list = []
    download_ids = args.id
    downloader = Downloader(args.saved_path, args.thread_num, args.timeout)
    for id in download_ids:
        info = nhentai_parser(id)
        task_list.append(nhentai(downloader=downloader, **info))

    for task in task_list:
        task.download()


if __name__ == '__main__':
    Watcher()
    main()
