#!/usr/bin/python3
import re,json,os,asyncio,time,datetime,threading
from urllib import request
class download():
    param = []
    headers={
            'Host':'www.nwxs8.com',
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language':'en-US,en;q=0.5',
            'Accept-Encoding':'gzip, deflate, br',
            'Connection':'keep-alive',
            'Cookie':'X_CACHE_KEY=012ffa03d41338b40c388b17763ed088; Hm_lvt_1b67fa8737e6a6f82f73431711dbce90=1659513585; Hm_lpvt_1b67fa8737e6a6f82f73431711dbce90=1659513585; _ga=GA1.2.1652327722.1659513586; _gid=GA1.2.111647823.1659513586',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'cross-site',
            'If-Modified-Since':'Sun, 10 Apr 2022 14:55:32 GMT',
            'If-None-Match':'W/"6252efe4-32e2"',
            "Upgrade-Insecure-Requests": 1,
            }

    def setHeader(self,header):
        self.headers = header

    def run(self):
        self.downs(self.param)

    def get(self,url):
        req = request.Request(url,headers=self.headers)
        recv = request.urlopen(req,timeout=10)
        return recv

    def checkWeb(self,url):
        try:
            req = request.Request(url)
            recv = request.urlopen(req,timeout=2)
            return True
        except BaseException as e:
            return False



