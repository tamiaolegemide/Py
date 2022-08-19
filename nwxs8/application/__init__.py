#!/usr/bin/python3
import re,json,os,asyncio,time,datetime,threading,shutil
from urllib import request
from classes import filter,download
from interface import interface




APP_PATH  = os.path.dirname(os.path.abspath(__file__))
DL = "/"




webPre="https://www.nwxs8.com/news"
down = download.download()
content = down.get(webPre)
print(content)

'''

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



exit(1)


    recordUrl = "../data/record"
    downLoadUrl = "../Download"
    txtUrl = "../Txt"
    maxThread = 10
    #while maxThread > 0:

    def index(self):
        with open("../data/url") as f:
            urls = f.readlines()
            f.close()

        with open("../data/record","w+") as record:
            record_id  = record.read()
            record.close()

        if not isinstance(record_id,int) :
                record_id = 0

        i = record_id
        while True:
            curThread = threading.active_count() - 1
            if curThread < 10:
                with open(self.recordUrl,"w") as f:
                    f.write(str(i))
                obj = download()
                urlinfo = urls[i]
                pat = urlinfo.split("|")
                if pat[2].strip() == "0":
                    url = "https://www.nwxs8.com/news/" + pat[0].strip() + ".html"
                    filename = pat[1].strip()
                    filename = filename.replace("&nbsp;","_")
                    obj.setDownParam([url,filename])
                    maxThread  = obj.start()
                i+=1
            else:
                pass

            time.sleep(1)
        print("download finish")

    def getHtmlUrl():
        obj = download()
        obj.getLists()

    def getTxt(self):
        files = os.listdir(self.downLoadUrl)
        for folder in files:
            htmlHolder = os.listdir(self.downLoadUrl + "/" + folder);
            content = ""
            for i in range(1,len(htmlHolder)):
                filePath = self.downLoadUrl + "/" + folder + "/" + str(i) + ".html" 
                content += self.getTxtContent(filePath)
            targetPath = self.txtUrl + "/" + folder +".txt"
            with open(targetPath,"w+") as f:
                f.write(content)

    def getTxtContent(self,url):
        with open(url,"r") as f:
            content = f.readlines()
            content = content[86:]
            txt = '';
            for i in content:
                rs = re.search('<script src="/js/arc.js"></script>',i)
                if rs == None:
                    i = i.replace("<br>","")
                    txt += i
                else:
                    break
            return txt
            
    def mkdir(self,dirName):
        dirNameUrl = self.txtUrl + "/" + dirName;
        if not os.path.exists(dirNameUrl):
            os.makedirs(dirNameUrl)


    def moveTxt(self):
        self.sourceFolder = "/mnt/hgfs/share/nwsx8_txt/Txt"
        self.targetFolder  = "/mnt/hgfs/share/nwsx8_txt/folder"
        txtLists = os.listdir(self.sourceFolder)

        n = 0
        x = 0
        for i in txtLists:
            if n >= 2000:
                x += 1
                n = 0
            
            sourceFile = self.sourceFolder + "/"  + i
            targetFolder = self.targetFolder + "/" + str(x) 
            if not os.path.exists(targetFolder):
                os.makedirs(targetFolder)


            targetFile = targetFolder + "/" + i
            shutil.move(sourceFile,targetFile)
            n+=1
    def fuck(self):
        print("fuck")





obj = main()
obj.moveTxt()





'''
