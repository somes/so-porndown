#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time   : 2021/7/22
# @Author : somes
# @File   : download.py

import os
import json

import config

download_dir = config.download_dir
aria2_proxy = config.aria2_proxy

if not os.path.exists('%s' % download_dir):
    os.mkdir('%s' % download_dir)


def start_download(download_list_path):
    aria2c_path = ('./aria2/aria2c')
    order = aria2c_path + aria2_proxy + ' -s8 -x8 -j3 -c -d "%s" -i ' % download_dir + download_list_path + ' -l "./aria2/aria2.log"'
    os.system(order)


def get_file():
    f = open('./json/json.txt').read()
    data_lists = json.loads(f)

    if os.path.isfile('./json/download-list.txt'):
        os.remove('./json/download-list.txt')

    for i in data_lists:
        status, num, title, url = i['status'], i['num'], i['title'], i['url']
        if status == 0:
            us = '%s\n out=%s.mp4\n' % (url, title)
            with open('./json/' + 'download-list' + '.txt', 'a') as f:
                f.writelines(us)


if __name__ == '__main__':
    get_file()
    start_download('./json/download-list.txt')
