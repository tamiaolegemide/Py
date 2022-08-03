#!/usr/bin/python3.8
import re,json,os,asyncio,time,datetime,threading
from urllib import request




class index():
    headers={
            
            "Referer":"https://www.qx192.com/jtll/index_1.html", 
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gizp,defale',
            'Accept-Language': 'zh-CN,zh;q=0.9'
            }
    def __init__(self):
        pass

    def getLists(self):
        pre = "https://www.qx192.com/jtll/index"
        for i in range(1,109):
            if i == 1:
                url = pre + ".html"
            else:
                url = pre + "_" + str(i) + ".html"
            req = request.Request(url,headers=self.headers)
            recv = request.urlopen(req,timeout=100)
            rs = recv.read().decode()
            with open("../log/record","a+") as f:
                f.write(str(i));
            self.getUrl(rs)



    def main(self):
        self.getLists()



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




    def getUrl(self,content):
        string = re.findall('<li class="list5">(.*?)</li>',content)
        n = 1
        with open("../config/urls","a+") as f:
            for i in string:
                url = re.search('"(/.*.html)"',i)
                name = re.search('title="(.*?)"',i)
                if url != None and name != None:
                    #print(url,name)
                    #print(url.group(0),name.group(0))
                    name = name.group(1)
                    url = url.group(0)
                    f.write(url+"|"+name + "\r\n")
                    #self.download(i)

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
        recv = request.urlopen(req,timeout=30)
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



obj = index()
obj.main()

