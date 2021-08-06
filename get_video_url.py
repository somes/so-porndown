#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time   : 2021/7/22
# @Author : somes
# @File   : get_video_url.py

import re
import requests
from lxml import etree
import demjson
import aiohttp

import config

req_proxy = config.req_proxy
aioh_proxy = config.aioh_proxy

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "cookie": "%s" % config.cookie
}

lists = []


async def Get_Page(url, n):
    timeout = aiohttp.ClientTimeout(total=330, connect=2, sock_connect=15, sock_read=10)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, verify_ssl=False),
                                     timeout=timeout) as session:
        response = await session.get(url, headers=headers, proxy=aioh_proxy)
        content = await response.read()

        Content = str(content, "utf-8")

        Title = etree.HTML(Content).xpath('//*[@class="inlineFree"]/text()')
        Title = re.sub("[\n\t\\\/:*?,，!！？。()（）.\"<=->|\]\[]", "", Title[0])

        JS = re.sub('[\n\t]', '', etree.HTML(Content).xpath('//*[@id="mobileContainer"]/script[1]/text()')[0])
        if re.findall('"mediaDefinitions":\[(\{.*?\})\],', JS):
            voll = re.findall('"mediaDefinitions":\[(\{.*?\})\],', JS)[0]
            volls = re.findall('\{.*?\}', voll)
            mp4_str, tls_str = volls[0], volls[1]
            dicts = demjson.decode(mp4_str)
            link = dicts['videoUrl']
            html = requests.get(link, headers=headers,
                                proxies=req_proxy).text
            print(n, Title)
            videoUrl = max(re.findall('"videoUrl":"(.*?)","', html)).replace('\/', '/')
            print(videoUrl)
            print('')
            status = 0
        else:
            print(n, '\033[32m' + str(Title) + '\033[0m')
            videoUrl = 'ERROR'
            print('\033[32m' + videoUrl + '\033[0m')
            print('')
            status = 1

        list = {"status": status, "num": n, "title": "%s" % Title, "url": "%s" % videoUrl}
        lists.append(list)
