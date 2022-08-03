#!/usr/bin/python3.6
#http://hxs6.com/zhongkouweixiaoshuo/
from pathlib import Path
from urllib import request
import re
import os

'''
for line in rs:
    string += line

g = re.search(r".*",string)
'''




#得到列表页
def getList(url):
    '''
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request("http://hxs6.com/zhongkouweixiaoshuo/",headers= head)
    p = request.urlopen(req)
    rs = p.read()
    '''
    articles = []
    req = request.Request(url)
    p = request.urlopen(req)
    rs = p.read().decode()
    suf = re.search("<li class=\"New\">.*</li>",rs)
    if suf is not None :
        pattern= re.compile(r"href=\"(.*?)\"")
        hrefSearch = pattern.findall(suf.group(0))
        for key in hrefSearch:
            rs = re.search("\.html",key)
            if rs is not  None:
                articles.append(key)
    return articles;


def getPage(page):
    page = "http://hxs6.com"+  page 
    #page = "http://hxs6.com/zhongkouweixiaoshuo/2019/0516/11750.html"
    req = request.Request(page)
    p = request.urlopen(req)

    content = p.readlines()


    string = ""

    key = False
    end = False


    title = None
    for s in content:
        s = s.decode()
        title_content = re.search("<title>(.*)</title>",s)
        if title_content is not None:
            title = title_content.group(1).replace("_H小说吧_H文_肉文_H小说在线阅读文库","")
            title = title.replace("【","");
            title = title.replace("】","");
            title = title.replace(" ","");
            title = title.replace("/","-");


        if(key and  not end):
            string +=s 
        if re.search("ART",s) is not None:
            key = True
        if key and re.search("</div>",s) is not None:
            end = True
    string = re.sub("<.*?>","",string);
    string = re.sub("&hellip;",".",string);
    newfile = open("./novel/"+title+".txt","w")
    newfile.write(string)
    return 0





num = 2
maxv = 29
cate = "renqiluanlun"

for i in range(maxv):
    n = i+1
    url = "http://hxs6.com/"+cate+"/list_"+str(num)+"_"+str(n)+".html"
    pages = getList(url)
    for key in pages:
        getPage(key)


