# -*- coding:UTF-8 -*-
import argparse
from logger import logger


def cmd_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--id', type=str, dest='id',
                        action='store', help='an id list for example 1,2,3')
    parser.add_argument('--path', type=str, dest='saved_path',
                        action='store', default='', help='path you want to download')
    parser.add_argument('--threads', '-t', type=int, dest='thread_num',
                        action='store', default=5, help='download thread number')
    parser.add_argument('--timeout', type=int, dest='timeout',
                        action='store', default=30, help='download timeout')
    parser.add_argument('--proxy', type=str, dest='proxy',
                        action='store', default='', help='use proxy, example: http://127.0.0.1:8080')
    args = parser.parse_args()

    if args.id:
        id_list = map(lambda id: id.strip(), args.id.split(','))
        args.id = set(map(int, filter(lambda id: id.isdigit(), id_list)))
    else:
        logger.critical('need id')
        parser.print_help()
        exit()

    if args.thread_num <= 0:
        args.thread_num = 1
    elif args.thread_num > 10:
        logger.critical('Maximum number of threads is 10')
        exit(0)

    if args.proxy:
        import urlparse
        proxy_url = urlparse.urlparse(args.proxy)
        if proxy_url.scheme not in ('http', 'https'):
            logger.error(
                u'Invalid protocol \'{0}\' of proxy, ignored'.format(proxy_url.scheme))
        else:
            from config import PROXIES
            PROXIES = {proxy_url.scheme: args.proxy}

    return args


if __name__ == '__main__':
    print cmd_parser()
