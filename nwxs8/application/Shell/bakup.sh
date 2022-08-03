#!/usr/bin/python3
import re,json,os,asyncio,time,datetime,threading,shutil
from urllib import request
from download import download

class main():
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





obj = main()
obj.moveTxt()



