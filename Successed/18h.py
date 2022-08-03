#!/usr/bin/python3.7
import re
import json
import socket
from urllib import request

def send(url,dirname,filename):
    HOST = '127.0.0.1'  # 服务器的主机名或者 IP 地址
    PORT = 65412 # 服务器使用的端口

    headers={"Referer":"http://18h.animezilla.com"}

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        rs = json.dumps({'url':url,"dirname":dirname,"name":filename,"headers":headers})
        s.sendall(rs.encode())
        data = s.recv(1024)

def getMangaUrl(content):
    manga_urls = []
    for i in content:
        rs = re.search("https://18h.animezilla.com/manga/\d{3,7}",i.decode())
        if rs is not None:
            getManagePage(rs.group(0))



def getManagePage(manga_url):
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
    maxPage = int(maxPage.group(1))

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


max = 19
url_priv = "https://18h.animezilla.com/manga/page/"

for i in range(19):
    n = i+1;
    page_url = url_priv+str(n)
    req = request.Request(page_url)
    p = request.urlopen(req)
    content = p.readlines()
    getMangaUrl(content)





