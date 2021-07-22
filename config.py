#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time   : 2021/7/22
# @Author : somes
# @File   : config.py

import configparser

file = 'config/config.ini'

conf = configparser.ConfigParser()
conf.read(file, encoding='utf-8')

# sections = conf.sections()
# print(sections)

user_ = dict(conf.items('user'))
proxy_ = dict(conf.items('proxy'))
path_ = dict(conf.items('path'))
cookie_ = dict(conf.items('cookie'))

'''user'''
user = user_['user']

'''proxy'''
proxy_on = int(proxy_['proxy_on'])
proxy_http_ip = proxy_['proxy_http_ip']
proxy_http_port = int(proxy_['proxy_http_port'])

'''path'''
download_dir = path_['download_dir']

'''cookie'''
cookie = cookie_['cookie']

if proxy_on == 0:
    req_proxy = {'http': 'http://%s:%d' % (proxy_http_ip, proxy_http_port),
                 'https': 'https://%s:%d' % (proxy_http_ip, proxy_http_port)}
    aioh_proxy = 'http://%s:%d' % (proxy_http_ip, proxy_http_port)
    aria2_proxy = " --https-proxy 'http://%s:%d'" % (proxy_http_ip, proxy_http_port)
else:
    req_proxy = None
    aioh_proxy = None
    aria2_proxy = ''
