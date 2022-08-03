
#!/usr/bin/python3.7
import re
import json
import socket
from urllib import request,error
from lxml import etree



class standdown:
    url = ''
    pageList  = []

    def test(self):
        urls = ["http://www.baidfs.com","http://www.baidu.com"]
        for i in urls:
            try:
                rs = request.urlopen(url=i)
                print(rs.status)
            except error.URLError as err:
                print(err.reason)


    def setUrl(self,url):
        self.url  = url


    def sendHttp(self,url):
        req = request.Request(url)
        p = request.urlopen(req)
        return  p.read().decode()


    def getLists(self):
        max = 1
        for i in range(max):
            if i == 0 :
                url = self.url +".html"
            else :
                url = self.url + "_" +  str(i+1)+".html"
            listContent = self.sendHttp(url)
            self.getPageUrl(listContent)



    def getPageUrl(self,content):
        for i in content: 
            title = re.search('href="(article/.*.html)"',i.decode()) 
            if title != None:
                #self.pageList.append(title.group(1))
                print(title.group(1))
                #self.getPageContent(title.group(1))



    def getPageTest(self):
        self.getPageContent(1)

    def getPageContent(self,url):
        content  = self.sendHttp(url)
        content = fs.read()
        title = re.search("<title>(.*)</title>",content);
        content = content.replace("<br>","");
        html = etree.HTML(content)
        a_tags = html.xpath('//*[@class="articleList"]')


        second = a_tags[1]
        div = second[1]
        article = div[2]

        with open("./novel/"+title.group(1)+".txt","w") as f:
            f.write(article.text)



    def getList(url):
        with open("list.html","r") as fs:
            content = fs.read()
            fs.close()
            headers={"Referer":"http://18h.animezilla.com"}
            req = request.Request(url,headers=headers)
            recv = request.urlopen(req)



        title = re.search("<title>(.*)</title>",content)
        title = title.group(1)
        title = title.replace(" ","")
        rs = re.search("-",title)
        if rs is not None:
            title = re.sub("-.*","",title)
        maxPage = re.search("\[(\d*)P\]",title)
        if maxPage is None: 
            maxPage = re.search("<a class=\"last\".*?\d{2,4}/(\d{2,4})\">",content) 
        maxPage = int(maxPage.group(1))
        ###



obj = standdown()
obj.setUrl("http://yazhouse8.com/l9kdK")
obj.test()
