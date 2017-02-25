# -*- coding:UTF-8 -*-
import os
import requests
import threadpool
from logger import logger
from singleton import Singleton
from urlparse import urlparse
from config import PROXIES


class Downloader(object):
    __metaclass__ = Singleton

    def __init__(self, saved_path, thread_num, timeout):
        self.saved_path = saved_path
        self.thread_num = thread_num
        self.threads = []
        self.timeout = timeout
        self.retry_count = 3

    def _download(self, url, folder='', filename='', retried=False):
        retried_count = self.retry_count
        logger.info(u'Start downloading: {0} ...'.format(url))
        filename = filename if filename else os.path.basename(
            urlparse(url).path)
        base_filename, extension = os.path.splitext(filename)
        while retried_count > 0:
            try:
                with open(os.path.join(folder, base_filename.zfill(3) + extension), "wb") as f:
                    response = requests.request('get', url, stream=True,
                                                timeout=self.timeout, proxies=PROXIES)
                    length = response.headers.get('content-length')
                    if length is None:
                        f.write(response.content)
                    else:
                        for chunk in response.iter_content(2048):
                            f.write(chunk)
                return url
            except requests.HTTPError as e:
                if not retried:
                    logger.error(u'Error: {0}, retrying'.format(str(e)))
                    retried_count -= 1
                else:
                    return None
            except Exception as e:
                logger.critical(str(e))
                return None

    def _download_callback(self, request, result):
        if not result:
            logger.critical(u'Unexpected error occurred')
            exit(1)
        logger.info(u'{0} download successfully'.format(result))

    def download(self, queue, mangaid):
        folder = str(mangaid)
        if self.saved_path:
            folder = os.path.join(self.path, folder)

        if os.path.exists(folder):
            logger.warn(u'Path \'{0}\' already exist.'.format(folder))
        else:
            logger.warn(u'Path \'{0}\' not exist.'.format(folder))
            try:
                os.makedirs(folder)
            except EnvironmentError as e:
                logger.critical(u'Error: {0}'.format(str(e)))
                exit(1)

        queue = [([url], {'folder': folder}) for url in queue]

        self.thread_pool = threadpool.ThreadPool(self.thread_num)
        requests_ = threadpool.makeRequests(
            self._download, queue, self._download_callback)
        for req in requests_:
            self.thread_pool.putRequest(req)
        self.thread_pool.wait()
