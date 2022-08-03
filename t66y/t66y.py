#!/usr/bin/python3.7
import re,json,os,asyncio,time,datetime,threading
from urllib import request




class t66y():
    headers={
            "Referer":"https://cb.wpio.xyz/thread0806.php",
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
            'Referer': 'https://www.zhaopin.com/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gizp,defale',
            'Accept-Language': 'zh-CN,zh;q=0.9'
            }
    def __init__(self):
        pass

    def getLists(self):
        pre = "https://cb.wpio.xyz/thread0806.php?fid=20&search=&page="
        for i in range(21,25):
            print(i)
            url = pre + str(i)
            req = request.Request(url,headers=self.headers)
            recv = request.urlopen(req,timeout=10)
            self.getPage(recv.read().decode("gbk"))



    def fuck(self):
        files = os.listdir("./novel") 
        for i in files:
            with open("./novel/"+i,"rb") as f:
                html = f.read().decode("gbk",errors="ignore")
                contents = re.findall('<div class="tpc_content do_not_catch">(.*?)</div>',html)
                content = contents[0]
                content = content.replace("<br>","\r")
                content = content.replace("&nbsp;","")
                content = content.replace("&quot;","\"")
                f.close()

            with open("./novel/"+i,"w") as f:
                f.write(content)
                f.close()



    def checkZero(self):
        with open("url","r") as f:
            urls = f.readlines()
            f.close()
        with open("zero","r") as f:
            zeros = f.readlines()
            f.close()

        has=[]
        no = []
        names=[]
        ish =False
        for i in zeros:
            ish =False
            for j in urls:
                pat = j.split("|")
                if pat[1].strip() == i.strip():
                    self.download([pat[0].strip(),pat[1].strip()])
                    ish = True
            if ish is False:
                no.append(i)



    def getList(self):
        with open("url") as f:
            urls = f.readlines()
            f.close()
            for i in range(0,len(urls)):
                obj = urls[i]
                pat = obj.split("|")
                if pat[2].strip() == "0":
                    url = pat[0].strip()
                    filename = pat[1].strip()
                    filename = filename.replace("&nbsp;","_")
#                    self.download([url,filename])
                    print(i)
                    urls[i] = url+"|" + filename + "|1\r\n"
                    self.save(urls)


    def save(self,urls):
        with open("url","w") as f:
            for i in urls:
                f.write(i)
            f.close()





    def getPage(self,content):
        string = re.findall('<h3><a href="(htm_data.*?\.html)" target="_blank" id="">(.*?)</a></h3>',content)
        with open("./url","a+") as f:
            for i in string:
                filename = i[1].strip()
                rs = re.search("<",filename)
                if rs == None:
                    f.write(i[0]+"|"+filename+"|0""\r\n")
                    #self.download(i)
            f.close()


    def download(self,i):
        pre= "https://cb.wpio.xyz/"
        url = pre + i[0]
        filename = i[1].replace("&nbsp;","_")
        req = request.Request(url,headers=self.headers)
        recv = request.urlopen(req,timeout=10)
        with open("./url","a+") as d:
            d.write(i[1]+"|"+i[0]+"\r\n")
            d.close()
        try:
            html = recv.read()
            content= html
            contents = re.findall('<div class="tpc_content do_not_catch">(.*?)</div>',html.decode("utf-8"))
            content = content.replace("<br>","\r")
            content = content.replace("&nbsp;","")
            content = content.replace("&quot;","\"")
        except BaseException as e:
            with open("./error","a+") as d:
                d.write("解误失败|"+i[1]+"|"+i[0]+"\r\n")
                d.close()
        try:
            with open("./novel/"+filename+".txt","wb") as f:
                f.write(content)
                f.close()
        except BaseException as e:
            with open("./error","a+") as d:
                d.write("保存失败|"+i[1]+"|"+i[0]+"\r\n")
                d.close()

        #print(recv.read().decode("gbk"))



obj = t66y()
obj.fuck()

