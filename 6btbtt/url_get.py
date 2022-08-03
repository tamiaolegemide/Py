#!/usr/bin/python3.7
import re
import json
import socket
import random
import string
import os
import asyncio
import threading
from urllib import request





def getlist():
    for i in range(39):
        n = i+1;
        url_priv = "http://www.6btbtt.com/forum-index-fid-8-page-"+str(n)+".htm"
        getpage(url_priv)

def getpage(url):
    #print(url)
    req = request.Request(url)
    p = request.urlopen(req)
    ls = p.readlines()
    for i in ls:
        geturl(i.decode())


def geturl(content):
    #http://www.6btbtt.com/thread-index-fid-8-tid-10982.htm
    url = re.search("href=\"(.*thread-index-fid-.*?)\"",content)
    if url != None:
        page_url = url.group(1)
        getzip(page_url)

def getzip(url):
    #url = "http://www.6btbtt.com/thread-index-fid-8-tid-28237.htm"
    #url = "http://www.6btbtt.com/thread-index-fid-8-tid-28237.htm"
    req = request.Request(url)
    p = request.urlopen(req)
    
    ls = p.readlines()
    obj = download()
    for i in ls:
        rs = re.search("href=\"(.*attach-dialog-fid.*?)\"",i.decode())
        if rs is not None:
            ajax_url = rs.group(1)
            obj.setUrl(ajax_url)
            obj.start()
            print(threading.get_ident())
            #time.sleep(3)

            #attach-dialog-fid-8-aid-164795-ajax-1-ajax-1.htm
    #http://www.6btbtt.com/attach-dialog-fid-8-aid-164795-ajax-1.htm



class download(threading.Thread):
    url  = ""
    def setUrl(self,url):
        self.url = url
    def run(self):
        req = request.Request(self.url)
        p = request.urlopen(req)
        js = json.loads(p.read())
        body = js['message']['body']
        rs = re.search("href=\"(.*attach-download-fid-8-ai.*?)\"",body)
        if rs is not None:
            req = request.Request(rs.group(1))
            p = request.urlopen(req)
            filename = self.ranstr(20) + ".rar"
            with open(filename,"wb+") as f:
                f.write(p.read())

    def ranstr(self,num):
        salt = ''.join(random.sample(string.ascii_letters + string.digits, num))
        if os.path.exists(salt) :
            return self.ranstr(num)
        else:
            return salt

getlist()
