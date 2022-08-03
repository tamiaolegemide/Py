#!/usr/bin/python3.7
import re,json,socket,os,asyncio,time,datetime,threading
from urllib import request
from urllib.parse import quote
import  string

def record(string):
    with open("record","a+") as fs:
        fs.write(string+"\n")

def getmax(ar):
    n = 0
    for i in ar:
        if int(i) > int(n) :
            n = i
    return int(n)


def gethtml(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    print(url)
    exit(1)
    url = quote(url, safe = string.printable)   # safe表示可以忽略的字符
    exit(1)
    print(url)
    exit(1)
    req =  quoter.Request(url,headers=headers)
    rs = request.urlopen(req)
    rs = rs.read().decode()
    print(rs)
    exit(1)


def getlist(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    url="http://www.yylyyl8.com/detail/Beautyleg_%E7%AC%AC%E5%8D%81%E4%BA%94%E9%9B%86_015Jellyfish.html"
    url = quote(url, safe = string.printable)   # safe表示可以忽略的字符
    req = request.Request(url,headers=headers)
    rs = request.urlopen(req)
    con = rs.read().decode()
    with open("a.html","w") as f:
        f.write(con)
    exit(0)








def getpage(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = request.Request(url,headers=headers)
    rs = request.urlopen(req)
    con = rs.read().decode()
    rep = re.compile(r"<a id=\"ha\".* href=\"(/detail/.*\.html).*")
    group = rep.findall(con)
    prix ="http://www.yylyyl8.com"
    getlist(prix+group[0])



prix = "http://www.yylyyl8.com/clist/"
for i in range(1,33):
    url = prix+""+str(i)
    getpage(url)




'''
url = "http://www.yylyyl8.com/"
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
req = request.Request(url,headers=headers)
p = request.urlopen(req)
'''





'''
con = p.read()
rs = str(con, encoding="utf-8")
rep = re.compile(r"<a id=\"ha\".* href=\"(/detail/.*\.html).*")
group = rep.findall(rs)
for i in group:
    record(i)

'''






#    <a id="ha" href="/detail/经典写真_228-108TV金雨佳_–_108酱重磅推荐S级美女(1).html" title="经典写真 经典写真228-108TV金雨佳–108酱重磅推荐S级美女(1)" target="_self" class="r9">

