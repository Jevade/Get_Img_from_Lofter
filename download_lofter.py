# -*- coding:utf8 -*-
from bs4 import BeautifulSoup
import re
import requests
from datetime import datetime
import random
import time
from multiprocessing.managers import BaseManager
import sys
import os

if sys.version_info[0] == 3:
    from urllib.request import urlopen, urlretrieve
    import queue
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen
    from urllib import urlretrieve
    import Queue as queue


def get(fun):
    print('My name is:')
    return fun


@get
def showName(name):
    print('' + name)

class Img(object):
    imgid = 0

    def __init__(self, imgid=0):
        self.imgid = imgid

    def getImg(self, task, fail, outDir='.'):

        thetask = task.get(timeout=1)
        posturl, imgurl, page, num, name = thetask[
                                               0], thetask[1], thetask[2], thetask[3], thetask[4]

        outDir = os.path.join(outDir, name)

        if os.path.isdir(outDir):  # 不用加引号，如果是多级目录，只判断最后一级目录是否存在
            print('dir exists')
            pass
        else:
            print('dir not exists')
            os.mkdir(outDir)
        path = os.path.join(outDir, 'page_{0}_img{1}.jpg'.format(page, num, ))
        print(path)
        if os.path.isfile(path):
            return 'file exist'
        else:
            try:
                urlretrieve(imgurl, path)
                return 'success'
            except:
                fail.put(thetask)
                return 'fail'


def getUrlPage(page):
    pass

def get_html(url):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,es;q=0.2,ru;q=0.2',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    html = requests.get(url, headers=header).text
    return html

def trasUrl(page,name='sys-peter'):
    return 'http://{0}.lofter.com/?page={1}'.format(name, page,)



def getUrlImg(page, task, name='sys-peter'):
    url = trasUrl(page,name)
    print(url)
    html = get_html(url)
    soup = BeautifulSoup(html)
    posturls = []
    imgurls = []
    print('run task %s...' % (url,))
    try:
        divs = soup.find_all('div', class_='pic')+soup.find_all('div', class_='img')
        num = 0
        if not divs:
            return False
        for div in divs:
            num += 1
            a = div.find('a', class_='img') if div.find('a', class_='img') else div.find('a')
            img = a.find('img')
            posturl = 'http:' + a.attrs['href'].split('http:')[-1]
            imgurl = img.attrs['src']
            task.put((posturl, imgurl, page, num, name))
            print('task {0} put'.format(posturl, ))
        return True
    except:
        return False
