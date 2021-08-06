#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time   : 2021/7/22
# @Author : somes
# @File   : favorites.py

import requests
from bs4 import BeautifulSoup
import asyncio
import os
import json

import get_video_url

import config

req_proxy = config.req_proxy
user = config.user

headers = {
    "referer": "https://cn.pornhub.com/",
    "path": "/users/%s/videos/favorites" % user,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
}


def Get_Page(x):
    Page = requests.get(x, headers=headers, proxies=req_proxy, timeout=5)
    Page.encoding = "utf-8"
    Page = Page.content
    return Page


html = Get_Page('https://cn.pornhub.com/users/%s/videos/favorites' % user)
soup = BeautifulSoup(html, 'lxml')
videoUList = soup.find('div', class_='videoUList').find_all('li')

loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(
        get_video_url.Get_Page(('https://cn.pornhub.com' + url.find('span', class_='title').a['href']), i + 1))
    for i, url in enumerate(videoUList)]
loop.run_until_complete(asyncio.wait(tasks))

print('页面数量: {}'.format(len(videoUList)))

lists = get_video_url.lists
json_data = json.dumps(lists)

print('列表数量: {}'.format(len(lists)))

if not os.path.exists('./json'):
    os.mkdir('./json')
with open('./json/' + 'json' + '.txt', 'w') as f:
    f.write(json_data)
