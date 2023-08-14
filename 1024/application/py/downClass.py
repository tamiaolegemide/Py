#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
import re,json,os,asyncio,time,datetime,threading,html,ssl
from datetime import date
from urllib import request
import shutil
from filters import getFilters




class downClass(threading.Thread):
    ic =""
    i= ""
    cacheUrl = "../data/cache/"
    logUrl = "../data/log/"
    urlFile = logUrl + "url"
    dataFile = logUrl + "data.js"
    timeout = 5

    magnetArr = []
    headers= {}

    def run(self):
        print(threading.get_ident(),threading.active_count())
        self.getDownUrl(self.ic,self.i[1]);



    def startNewThread(self,ic,i):
        self.ic =ic
        self.i = i


    def setHeader(self,headers):
        self.headers = headers



# 得到下载页面
    def getDownUrl(self,content,title):
        if content == False:
            return False
        content = html.unescape(content)
        string = re.findall('(https://down\.dataaps\.com\/list.php\?name=\w{1,32})',content)
        urls = []
        for i in string:
            content = self.getUrlContent(i)
            url = self.getMagnet(content)
            if url != False:
                if url not in urls:
                    urls.append(url)


        for url in urls:
            with open(self.urlFile,"a+") as f:
                f.write(url + "\n")


# 得到下载链接
    def getMagnet(self,content):
        if content == False:
            return False 
        string = re.findall('href="(magnet:\?xt=urn:btih:.*)"',content);
        if string == []:
            return False

        url = string[0]
        return url




    def download(self,url):
        req = request.Request(url,headers=self.headers)
        recv = request.urlopen(req,timeout=self.timeout)
        return recv


    def getUrlContent(self,url):
        rs = False
        ssl._create_default_https_context = ssl._create_unverified_context
        try:
            req = request.Request(url,headers=self.headers)
            recv = request.urlopen(req,timeout=self.timeout)
            rs = recv.read().decode()
        except Exception:
            pass
        return rs 





