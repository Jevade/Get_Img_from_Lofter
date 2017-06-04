#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Jevade on 2017/5/27
import re
import sys
import os

reload(sys)
from Tkinter import *
from ScrolledText import ScrolledText

sys.setdefaultencoding('utf-8')
import threading
import requests
import urllib
import BeautifulSoup as bs4

BASE_DIR = os.getcwd() + "/video"
url_name = []


def getPornVedio(*args, **kwargs):
    global id
    id = 0
    print args
    for url in args[0]:
        id = id + 1
        urllib.urlretrieve(url, os.path.join(BASE_DIR, "%s_%d.mp4") % ('porn', id))


def getPornurl():
    head = {"Accept": "* / *",
            "Accept - Encoding": "identity",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,es;q=0.2,ru;q=0.2",
            "Connection": "keep - alive",
            "DNT": "1",
            "Host": "dm.phncdn.com",
            "Range": "bytes = 0 -",
            "Referer": "https: // www.pornhub.com / view_video.php?viewkey = ph56155f250bf20",
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
            }
    url = "https://dm.phncdn.com/videos/201510/07/58929281/vl_480P_271.0k_58929281.mp4?ttl=1495904143&ri=1024000&rs=384&hash=c0c02be6ae03860f1d59a74cde9134ea"
    url2 = "https://bd.phncdn.com/videos/201610/27/94210272/480P_600K_94210272.mp4?ipa=45.35.75.57&rs=200&ri=2500&s=1495898553&e=1495905753&h=1867bd9f14fa4a8333578ff5ed85ed15"
    urls = [url, url2]
    # html = requests.get(url, headers=head)

    th = threading.Thread(target=getPornVedio, args=(urls,))
    th.start()
    print(123)


def getURL():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    url = 'http://www.budejie.com/video/'
    html = requests.get(url, headers=header).text
    # html2 = urllib.urlopen(url)
    url_content = re.compile(
        r'(<div class="j-r-list-c">.*?</div>.*?</div>)', re.S)
    url_contents = re.findall(url_content, html)
    id = 1
    for i in url_contents:
        # print i
        url_reg = r'data-mp4="(.*?)"'
        url_items = re.findall(url_reg, i)
        if url_items:
            detail_reg = re.compile(r'<a href="/detail-.{8}?.html">(.*?)</a>', re.S)
            detail_reg_content = re.findall(detail_reg, i)
            for i, k in zip(detail_reg_content, url_items):
                url_name.append([i, k])
    return url_name


def get():
    url_name = getURL()
    global id
    id = 1
    for item in url_name:
        urllib.urlretrieve(item[1], os.path.join(BASE_DIR, "%s.mp4") % (item[0]))
        varl.set(item[0])
        text.insert(END, str(id) + '.' + item[1] + '\n' + item[0] + '\n')
        id = id + 1
    varl.set("抓取完毕")


def start():
    th = threading.Thread(target=get)
    th.start()



def getaqyVedio():
    head = {"Accept": "* / *",
            "Accept - Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,es;q=0.2,ru;q=0.2",
            "Connection": "keep - alive",
            "DNT": "1",
            "Host": "http://www.iqiyi.com",
            "Referer": "http://www.iqiyi.com/v_19rr7d6p3s.html?fc=82992814760eeac6",
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
            }
    url = "http://124.193.0.138/videos/v0/20170525/3b/cd/b17a6785a65a2b354218ad2e30cb534e.f4v?key=076bc558b235d3fbb4de75bc2ea985ab7&dis_k=0c0b45a3dc948d4ce2a75898b29f9ff3e&dis_t=1496020529&dis_dz=GWBN-BeiJing&dis_st=42&src=iqiyi.com&uuid=dbefe3f6-592b7631-e9&rn=1496020529004&qd_ip=dbefe3f6&qd_aid=685882100&vid=40e81aa1bdd373aca729ce95175b1514&pv=0.1&qyid=y9pu0odbmpgg5ahdj3tmvvou&qd_vipdyn=2&qd_vip=0&ibt=9a0154f60312e06d209e2a88125fb78d&qd_uid=0&qd_k=5d24615a72bce8f9c79e3a69b287a4b2&cross-domain=1&ptime=360000&QY00001=1023108576&pri_idc=beijing10_dxt&qd_stert=0&qypid=&qd_p=dbefe3f6&qd_tvid=685882100&cid=afbe8fd3d73448c9&qd_index=1&qd_src=01010031010000000000&qd_tm=1496020526504&ib=4&qd_vipres=2&id=845737841564&range=8192-9068543"
    urllib.urlretrieve(url, os.path.join(BASE_DIR, "%s_%d.mp4") % ('aqy', 3))


getaqyVedio()
getPornurl()
root = Tk()
root.title('python下载视频')
text = ScrolledText(root, font=('微软雅黑', 10))
text.grid()
varl = StringVar()
button = Button(root, text='开始爬取', font=('微软雅黑', 10), command=start)
button.grid()
lable = Label(root, font=('微软雅黑', 10,), fg='blue', textvariable=varl)
lable.grid()
varl.set('虫虫已准备好')
root.mainloop()

# 应对网站的反扒机制，需要在request中加入头部信息 header
