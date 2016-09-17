# -*- coding:UTF-8 -*-
from config import IMAGE_URL
from logger import logger
from downloader import Downloader


class nhentai(object):

    def __init__(self, id, img_id, ext, pages, title, subtitle, downloader, **kwargs):
        self.id = id
        self.name = title
        self.img_id = img_id
        self.ext = ext
        self.pages = pages
        self.downloader = downloader

    def download(self):
        logger.info(u'Get nhentai manga named {}'.format(self.name))
        if isinstance(self.downloader, Downloader):
            download_queue = []
            for page in range(1, self.pages + 1):
                download_queue.append('{0}{1}/{2}.{3}'.format(
                    IMAGE_URL, self.img_id, page, self.ext))
            self.downloader.download(download_queue, self.id)
        else:
            logger.critical(u'Downloader load error')
