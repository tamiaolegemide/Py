#!/usr/bin/python3.8
import re,json,os,asyncio,time,datetime,threading
from urllib import request




class download():
    preurl = "https://bbs.cp50085.com/2048/"
    magnetArr = []
    headers={
#            "Referer":"https://cb.wpio.xyz/thread0806.php",
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
            'Referer': 'https://www.zhaopin.com/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gizp,defale',
            'Accept-Language': 'zh-CN,zh;q=0.9'
            }
    def __init__(self):
        pass

    def getPageUrl(self,i):
        return " https://bbs.cp50085.com/2048/thread.php?fid-3-page-"+ str(i) +".html";

    def genHtml(self):
        include "index.html"

obj = download()
obj.genHtml()

