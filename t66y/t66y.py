#!/usr/bin/python3
import re,json,os,asyncio,time,datetime,threading
from urllib import request




class t66y(threading.Thread):
    headers={
            "Referer":"https://cb.wpio.xyz/thread0806.php",
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gizp,defale',
            'Accept-Language': 'zh-CN,zh;q=0.9'
            }
    pageListUrl = ""
    startPage = 1;
    startLen = 2;

    def __init__(self):
        pass

    def getLists(self):
        pre = "https://cb.wpio.xyz/thread0806.php?fid=20&search=&page="


        for i in range(21,25):
            url = pre + str(i)
            req = request.Request(url,headers=self.headers)
            recv = request.urlopen(req,timeout=10)
            self.getPage(recv.read().decode("gbk"))


    def pageList(self,pageListUrl):
        self.pageListUrl = pageListUrl
        for i in range(self.startPage,self.startLen+1):
            url = "https://t66y.com/thread0806.php?fid=15&search=&page=" + str(i)
            url = "https://t66y.com/thread0806.php?fid=5&search=&page=" + str(i)
            self.getPageUrl(url)




    def getPageUrl(self,url):
        print("START:  " + url)
        content = self.download(url)
        lists = re.findall("htm.*?\.html",content);
        matchs = re.match("https://.*?\/",url)
        website = matchs.group(0);
        print("WEBSITE: "  + website)
        #website = website.replace("https","http");
        for i in lists:
            pageurl = website+i;
            print("PAGEURL:   " + pageurl )
            pageContent = self.download(pageurl);
            matchs = re.search("http://www.rmdown.com/.*?\"",pageContent)
            if matchs is not None:
                with open("./link","a+") as fs:
                    link = matchs.group()
                    link = link.replace("\"","")
                    print(link)
                    fs.write(link+"\n")





    def save(self,urls):
        with open("url","w") as f:
            for i in urls:
                f.write(i)
            f.close()



    def download(self,url):
        req = request.Request(url,headers=self.headers)
        recv = request.urlopen(req,timeout=10)
        try:
            html = recv.read().decode()
            return html

        except BaseException as e:
            print("error" + url)
        #print(recv.read().decode("gbk"))


pageUrl = "//https://t66y.com/thread0806.php?fid=15"
obj = t66y()
obj.pageList(pageUrl)

