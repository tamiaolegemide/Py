#!/usr/bin/python3.7
import re
import json
import socket
import os
import asyncio
from urllib import request




def getManagePage(manga_url):
    manga_url = re.sub("\n","",manga_url)
    req = request.Request(manga_url)
    p = request.urlopen(req)
    content = p.read().decode()
    title = re.search("<title>(.*)</title>",content)
    title = title.group(1)
    title = title.replace(" ","")
    rs = re.search("-",title)
    if rs is not None:
        title = re.sub("-.*","",title)
    maxPage = re.search("\[(\d*)P\]",title)
    if maxPage is None: 
        maxPage = re.search("<a class=\"last\".*?\d{2,4}/(\d{2,4})\">",content) maxPage = int(maxPage.group(1))
    maxPage +=1


    img_src = re.search("<img id=\"comic\" class=\"loading\".*?src=\"(.*?)\">",content)
    img_src = img_src.group(1)
    #send(img_src,title,1)

    for i in range(1,maxPage):
        next_url = manga_url+"/"+str(i+1)
        req = request.Request(next_url)
        p = request.urlopen(req)
        content = p.read().decode()
        img_src = re.search("<img id=\"comic\" class=\"loading\".*?src=\"(.*?)\">",content)
        img_src = img_src.group(1)
        send(img_src,title,int(i))
    return True




def send(url,dirname,name):
        dirname = dirname.replace("/","-")
        rs = os.path.exists("./"+dirname)
        if rs == False:
            os.mkdir(dirname)
        
        groups = re.search("\.(.{1,4})$",url)
        if groups:
            suf = groups.group(1)

        if name:
            filename = str(name) + "." + suf
        else:
            groups = url.split("/")
            filename = groups[len(groups)-1]


        isfile = os.path.isfile("./"+dirname+"/"+filename)
        if isfile is True:
            return True

        fs = open("result","a+")
        fs.write(url+" | " + dirname + " | " + str(name) +"\n")
        fs.close()


        headers={"Referer":"http://18h.animezilla.com"}
        req = request.Request(url,headers=headers)
        recv = request.urlopen(req)


        fs = open("./"+dirname+"/"+filename,"wb")
        fs.write(recv.read())
        fs.close()
        return True




fs = open("url","r");
urls = fs.readlines()
fs.close()
arr = {}
n = 0
for i in urls:
    arr[i] = 0 


rs = os.path.isfile("./json")
if rs is False:
    fs=open("json","w+")
    fs.close()

fs = open("json","r+")
urls = fs.read()
fs.close()

if urls is not "":
    urls = json.loads(urls)
    for url in urls:
        if urls[url] == 0:
            rs = getManagePage(url)
            if rs == True:
                urls[url] = 1
                with open("json","w") as fs:
                    fs.write(json.dumps(urls))
else:
    for url in arr:
        rs = getManagePage(url)
        if rs == True:
            arr[url] = 1
            with open("json","w") as fs:
                fs.write(json.dumps(arr))
    fs.close()







