#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
import re,json,os,asyncio,time,datetime,threading,html
from datetime import date
from urllib import request
import shutil
from filters import getFilters




class downClass(threading.Thread):
    ic =""
    i= ""

    timeout = 5
    listId = 0 #the number of webs
    webs = [
            "woniangzi.com",
            "healthwol.com",
            'woniangzi.com',
            ]
    web = webs[listId]
    preurl = "https://" + web + "/2048/"
    #preurl = "https://nongrao.com/2048/"
#    preurl = "https://maojinwu.com/2048/"
    cacheUrl = "../data/cache/"
    logUrl = "../data/log/"
    urlFile = logUrl + "url"
    dataFile = logUrl + "data.js"

    magnetArr = []
    headers={
            'Host': web,
            'Referer':'https://'+ web +'/2048/thread.php?fid-3-page-1.html',
            'Cookie':'zh_choose=n; a22e7_lastvisit=317%091657608588%09%2F2048%2Fthread.php%3Ffid-3-page-1.html; a22e7_lastpos=F3; a22e7_ol_offset=241627; a22e7_threadlog=%2C3%2C',
            #'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Accept':'*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding':'gzip,deflate,br',
            'Alt-Used':'bbs.huieiv.com',
            'Connection':'keep-alive',
            'Sec-Fetch-Dest':'script',
            'Sec-Fetch-Mode':'no-cors',
            'Sec-Fetch-Site':'same-origin',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.34 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gizp,defale',
            'Accept-Language': 'zh-CN,zh;q=0.9'


            }

    def run(self):
        print(threading.get_ident(),threading.active_count())
        self.getDownUrl(self.ic,self.i[1]);



    def startNewThread(self,ic,i):
        self.ic =ic
        self.i = i





# 得到下载页面
    def getDownUrl(self,content,title):
        if content == False:
            return False
        content = html.unescape(content)
        string = re.findall('(https://down\.dataaps\.com\/list.php\?name=\w{1,32})',content)
        for i in string:
            content = self.getUrlContent(i)
            self.getMagnet(content);


# 得到下载链接
    def getMagnet(self,content):
        if content == False:
            return False 
        string = re.findall('href="(magnet:\?xt=urn:btih:.*)"',content);
        if string == []:
            return False

        url = string[0]
        with open(self.urlFile,"a+") as f:
            f.write(url + "\n")
        return url




    def download(self,url):
        req = request.Request(url,headers=self.headers)
        recv = request.urlopen(req,timeout=self.timeout)
        return recv


    def getUrlContent(self,url):
        rs = False
        try:
            req = request.Request(url,headers=self.headers)
            recv = request.urlopen(req,timeout=self.timeout)
            rs = recv.read().decode()
        except Exception:
            pass
        return rs 





