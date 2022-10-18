#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
import re,json,os,asyncio,time,datetime,threading
from datetime import date
from urllib import request
import shutil
from filters import getFilters




class download():
    timeout = 20
    web = "bbs.huieiv.com"
    preurl = "https://" + web
    #preurl = "https://nongrao.com/2048/"
#    preurl = "https://maojinwu.com/2048/"
    cacheUrl = "../data/cache/"
    logUrl = "../data/log/"
    urlFile = logUrl + "url"
    dataFile = logUrl + "data.js"

    magnetArr = []
    headers={
            'Host': web,
            'Referer':'https://nongrao.com/2048/thread.php?fid-3-page-1.html',
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
    def __init__(self):
        pass

    def getPageUrl(self,i):
        return self.preurl + "thread.php?fid-3-page-"+ str(i) +".html";

    def getLists(self):
        with open(self.urlFile,"w+") as f:
            f.write("")

        for i in range(1,2):
            url = self.getPageUrl(i);
            print(url)
            fileName = str(date.today())+"-"+str(i)
            if not self.exist(fileName):
                content = self.getUrlContent(url)
                if content is not False:
                    self.writeFile(fileName,content)
                else:
                    self.delData()
                    exit("无法连接服务器")
            else:
                content = self.readFile(fileName)
            print("getHtmlUrl")
            self.getHtmlUrl(content)

    def delData(self):
        lists = os.listdir(self.cacheUrl)
        for i in lists:
            target = self.cacheUrl + i
            os.remove(target)


    def getUrlContent(self,url):
        rs = False
        try:
            req = request.Request(url,headers=self.headers)
            recv = request.urlopen(req,timeout=self.timeout)
            rs = recv.read().decode()
        except Exception:
            pass

        return rs 


    def getHtmlUrl(self,content=''):
        #<a href="state/p/3/2209/7457042.html" target="_blank" id="a_ajax_7457042" class="subject">▲小隻馬▲新片首发▲最強有碼合集♂[0914]</a>&nbsp; </td>
        string = re.findall('<a href="(state.*?)".*?>(.*?)<',str(content))
        #string = ['state/p/3/2207/6713225.html']


        with open(self.logUrl + "folder","w+") as f:
            for i in string:
                st = i[0] + "|" + i[1] + "\r\n"
                f.write(st)

        i = input("请查看要下载的目录")
        os.system("vim ../data/log/folder")
        with open(self.logUrl + "folder","r") as f:
            lists = f.readlines()
            for i in lists:
                i = i.split("|")

                url = i[0].strip()
                url = self.preurl + url
                ic = self.getUrlContent(url);
                self.getDownUrl(ic,i[1]);




# 得到下载页面
    def getDownUrl(self,content,title):
        if content == False:
            return False
        string = re.findall('(https://down\.dataaps\.com\/list.php\?name=\w{1,32})',content)
        for i in string:
            content = self.getUrlContent(i)
            self.getMagnet(content);


# 得到下载链接
    def getMagnet(self,content):
        if content == False:
            return False 
        string = re.findall('href="(magnet:\?xt=urn:btih:.*)"',content);
        url = string[0]
        with open(self.urlFile,"a+") as f:
            f.write(url + "\n")
        return url




    def download(self,url):
        req = request.Request(url,headers=self.headers)
        recv = request.urlopen(req,timeout=self.timeout)
        return recv


    def downs(self,i):
        #pre = "https://www.nwxs8.com/"
        url = i[0]


        filename = i[1].replace("&nbsp;","_")
        req = request.Request(url,headers=self.headers)
        recv = request.urlopen(req,timeout=self.timeout)
        '''
        with open("./url","a+") as d:
            d.write(i[1]+"|"+i[0]+"\r\n")
            d.close()
        '''


        if os.path.exists("./novel/"+filename+".txt"):
            return True

        try:
            content= recv.read().decode("utf-8");
            total = re.findall('共(\d*)页',content)
            content = re.sub("<.*>","",content)
            content = re.sub("\","",content)
            content = re.sub("\r","",content)
            content = re.sub("\n","",content)
            content= re.sub("　　","\r\n    ",content)
            content = re.sub("var.*","",content)
            content = " " + content
            if total == []:
                total = [0]
            total = int(total[0])
            if total > 0:
                for i in range(1,total+1):
                    nextUrl = re.sub(".html","_"+str(i)+".html",url)
                    temp =  self.download(nextUrl).read().decode("utf-8");
                    temp = re.sub("<.*>","",temp)
                    temp = re.sub("\","",temp)
                    temp = re.sub("\r","",temp)
                    temp = re.sub("\n","",temp)
                    temp = re.sub("　　","\r\n  ",temp)
                    temp = re.sub("var.*","",temp)
                    content = content  +"\r\n   "+ temp

        except BaseException as e:
            with open("./error","a+") as d:
                d.write("解误失败|"+i[1]+"|"+i[0]+"\r\n")
                d.close()
        try:
            with open("./novel/"+filename+".txt","w") as f:
                f.write(content)
                f.close()
        except BaseException as e:
            with open("./error","a+") as d:
                d.write("保存失败|"+i[1]+"|"+i[0]+"\r\n")
                d.close()

        #print(recv.read().decode("gbk"))

    def genDataJs(self):
        urls = []
        with open(self.urlFile,"r+") as f:
            temp = f.readlines()
            rs = "var data = " + json.dumps(temp) + ";";
        with open(self.dataFile,"w") as f:
            f.write(rs)

    def readFile(self,name):
        url = self.cacheUrl + name
        rs = os.path.exists(url)
        if rs == True:
            with open(url,"r") as f:
                return f.read()
        else:
            return False

    def checkRepeat(self):
        arr = []
        with open(self.urlFile,"r") as f:
            urls = f.readlines()
            for i in urls:
                if i not in arr:
                    arr.append(i)

        with open(self.urlFile,"w") as f:
            for i in arr:
                f.write(i)

        

    def writeFile(self,name,content):
        url = self.cacheUrl + name
        with open(url,"w") as f:
            return f.write(content)
    
    def exist(self,name):
        url = self.cacheUrl + name
        return os.path.exists(url)

    def toFolder(self):
        sourcePath = "/mnt/hgfs/share/nwsx8_txt/Txt"
        targetPath = "/mnt/hgfs/share/nwsx8_txt/sort"
        filters = [
                ]

        n = 0
        f = 0

        listDir = os.listdir(sourcePath)

        for i in listDir:
            newName  = self.replaceName(i)


            if n >= 3000:
                f +=1 
                n = 0
            targetFolder = targetPath + "/" +  str(f) + "/"
            if os.path.exists(targetFolder) == False:
                os.makedirs(targetFolder)
            shutil.move(sourcePath + "/" + i, targetFolder + "/" + newName)
            n+=1

    def replaceName(self,name):
        filters = getFilters()
        for j in filters:
            if name.find(j) is not False:
                name = name.replace(j,filters[j])
        print(name)
        return name





obj = download()
print("getLists")
obj.getLists()
print("checkRepeat")
obj.checkRepeat()
print("genDataJs")
obj.genDataJs()
#obj.toFolder()
