#!/usr/bin/python3
import re,json,os,asyncio,time,datetime,threading
from urllib import request
class download(threading.Thread):
    downLoadUrl = "../Download/"
    logUrl = "../Logs/"
    errorUrl = logUrl  + "/error"
    historyUrl = "../Logs/history"
    urlUrl = "../data/url"
    param = []
    headers={
            "Referer":"https://cb.wpio.xyz/thread0806.php",
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
            'Referer': 'https://www.zhaopin.com/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gizp,defale',
            'Accept-Language': 'zh-CN,zh;q=0.9'
            }

    def getLists(self):
        pre = "https://www.nwxs8.com/news/page_"
        for i in range(1,2544):
            url = pre + str(i) +".html"
            recv = self.download(url)
            rs=recv.read().decode()
            self.getPage(rs)
#        self.getList()


    def run(self):
        self.downs(self.param)


    def save(self,urls):
        with open(self.urlUrl,"w") as f:
            for i in urls:
                f.write(i)
            f.close()





    def getPage(self,content):
        string = re.findall('<a href="/news/(\d*).html" title="(.*?)">',content)
        with open("../data/url","a+") as f:
            for i in string:
                filename = i[1].strip()
                rs = re.search("<",filename)
                if rs == None:
                    f.write(i[0]+"|"+filename+"|0""\r\n")
                    #self.download(i)
            f.close()

    def download(self,url):
        req = request.Request(url,headers=self.headers)
        recv = request.urlopen(req,timeout=10)
        return recv

    def checkWeb(self,url):
        try:
            req = request.Request(url)
            recv = request.urlopen(req,timeout=2)
            return True
        except BaseException as e:
            return False



### i : url,filename    page:第几页
    def downs(self,i,page=1,total = None):
        #pre = "https://www.nwxs8.com/"

        if page != 1:
            url = re.sub(".html","_"+str(page)+".html",i[0])
        else:
            url = i[0]

        filename = i[1].replace("&nbsp;","_")
        dirNameUrl = self.downLoadUrl + filename
        with open(self.historyUrl,"a+") as f:
            f.write("Start:" + filename + "\n")

        try:
            if not os.path.exists(dirNameUrl):
                os.makedirs(dirNameUrl)
        except BaseException as e:
            with open(self.errorUrl,"a+") as f:
                f.write("无法创建目录 : "+filename + "url:" + url);
            return False;

        fileUrl = dirNameUrl + "/" + str(page) + ".html"
        
        if not os.path.exists(fileUrl) or True:
            try:
                req = request.Request(url,headers=self.headers)
                recv = request.urlopen(req,timeout=10)
                content= recv.read().decode("utf-8");
                if total == None:
                    totalRe = re.findall("共(\d{1,3})页",content);
                    if totalRe == [] or totalRe == None:
                            total = 1
                    else:
                        total = totalRe[0]

                with open(fileUrl,"w+") as f:
                    f.write(content)

            except BaseException as e:
                with open(self.errorUrl,"a+") as d:
                    d.write("解误失败|"+i[1]+"|"+i[0]+ repr(e)+"\r\n")
                    d.close()


            page += 1;
            if int(page) <= int(total):
                self.downs(i,page)

        with open(self.historyUrl,"a+") as f:
            f.write("End:" + filename +"\n")

