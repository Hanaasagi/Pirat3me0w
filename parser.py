# -*- coding:UTF-8 -*-
import re
import requests
from config import DETAIL_URL
from BeautifulSoup import BeautifulSoup
from logger import logger

'''
<div id="cover">
            <a href="/g/173082/1/">
                <img src="//t.nhentai.net/galleries/972582/cover.jpg" alt="..." />
            </a>
        </div>
'''


def nhentai_parser(id):
    logger.info(u'Fetching manga information of id {0}'.format(id))
    url = '{0}{1}'.format(DETAIL_URL, id)
    try:
        response = requests.request('get', url).content
    except Exception as e:
        logger.critical(str(e))
        exit(1)

    html = BeautifulSoup(response)
    manga_info = html.find('div', attrs={'id': 'info'})

    title = manga_info.find('h1').text
    _ = manga_info.find('h2')
    subtitle = _.text if _ else ''

    manga = dict()
    manga['id'] = id
    manga['title'], manga['subtitle'] = title, subtitle

    manga_cover = html.find('div', attrs={'id': 'cover'})
    img_info = re.search(
        '/galleries/([\d]+)/cover\.(jpg|png)$', manga_cover.a.img['src'])
    manga['img_id'], manga['ext'] = img_info.groups()

    for _ in manga_info.findAll('div'):
        pages = re.search('([\d]+) pages', _.text)
        if pages:
            manga['pages'] = int(pages.group(1))
            break
    return manga


if __name__ == '__main__':
    dic = nhentai_parser(174127)
    for key in dic:
        print u'{0} => {1}'.format(key, dic[key])
    # Output
    # subtitle => (C90) [canaria (粉山カタ)] 君だけのポニーテール [中国翻訳]
    # title => (C90) [canaria (Konayama Kata)] Kimi Dake no Ponytail [Chinese] [瑞树汉化组]
    # img_id => 976886
    # id => 174127
    # ext => jpg
    # pages => 35