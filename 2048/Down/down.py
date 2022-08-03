#!/usr/bin/python3.8
import json,re,random,time
import html,os.path,threading
from urllib import request


def mkdirs(cata):
    try:
        catalog = "../data/" + str(cata) 
        if os.path.isdir("../data") == False:
            os.mkdir("../data")
        if os.path.isdir("../data/" + str(cata)) == False:
            os.mkdir("../data/" + str(cata))
        return True
    except Exception:
        return False



class down(threading.Thread):
    u_data = "../data"
    u_error = "../config/down_error";
    u_pid = "../config/down_pid";
    u_current = "../config/down_current";
    u_record = "../config/down_record"
    user_agent = [
            "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20", "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52" ]
    HEADER = {
            'User-Agent': random.choice(user_agent),  # 浏览器头部
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', # 客户端能够接收的内容类型
            'Accept-Language': 'en-US,en;q=0.5', # 浏览器可接受的语言
            'Connection': 'keep-alive', # 表示是否需要持久连接
            }

    def setParam(self,cata,pics,num):
        self.cata = cata
        self.pics= pics 
        self.num =num 

    def run(self):
        cata = self.cata
        pics = self.pics
        num = self.num

        if os.path.isdir(self.u_data) == False:
            os.mkdir(self.u_data)

        cata = self.filter(cata);
        dirpath = self.u_data +"/" +  str(cata)
        if os.path.isdir(dirpath) == False:
            #print(dirpath,os.path.isdir(dirpath))
            os.mkdir(dirpath)

        catalog = self.u_data + "/" + str(cata) 

        for i in pics:
            url = i
            url = html.unescape(url)
            urlArr = url.split(".")
            suffix = urlArr[len(urlArr)-1]

            groups = url.split("/")
            filename = groups[len(groups)-1]
            filename =  catalog + "/" + str(filename)
            if os.path.isfile(filename) == True:
                return True
            if os.path.isfile(filename) == True:
                return True

            try:
                ireq = request.Request(url,headers=self.HEADER)
                p = request.urlopen(ireq,timeout=60)
            except Exception:
                with open(u_error,"a+") as error:
                    error.write(str(cata)+"@"+url+"\n")
                    error.close()
                    continue

            icontent = p.read()
            if os.path.isfile(filename) == False:
                with open(filename,"wb") as img:
                    img.write(icontent)
                    img.close()
            with open(u_current,"w") as fs:
                d = fs.write(str(self.num))



    def filter(self,title): 
        filters = [ "！", "[", "]", "【", "】", "/" ," ","-" ,"2048核基地1024核工厂","，","卡通漫畫2048hjd2048.com","|","(",")"]
        if title is not None:
            for i in filters:
                title = title.replace(i,"");
                
            return title
        else:
            return False

    def init(self):
        if False == os.path.exists(u_current):
            with open(u_current,"w+") as fs:
                fs.write("")
                fs.close()



        with open(u_pid,"w+") as fs:
            pid= os.getpid()
            fs.write(str(pid))
            fs.close()

        with open(u_current,"r") as fs:
            d = fs.read()
            if d == "" or d == "\n":
                curCat=0
            else:
                curCat = int(d)
        num=0


    def checkName(self):
        with open("../config/urls","r") as fs:
            while True:
                lines = fs.readline()
                try:
                    datas = json.loads(lines)
                except Exception:
                    continue
                title = datas['title']
                pics = datas['pics']
                title = self.filter(title)
                if title == False:
                    with open("../config/dir_wrong","a+") as dirs:
                        dirs.write(str(title)+"\n")

                else:
                    rs=mkdirs("../data/" + title)
                    with open("../config/dir_wrong","a+") as dirs:
                        if rs == False:
                            dirs.write(str(title)+"\n")




u_data = "../data"
u_error = "../config/down_error";
u_pid = "../config/down_pid";
u_current = "../config/down_current";


if False == os.path.exists(u_current):
    with open(u_current,"w+") as fs:
        fs.write("")
        fs.close()



with open(u_pid,"w+") as fs:
    pid= os.getpid()
    fs.write(str(pid))
    fs.close()

with open(u_current,"r") as fs:
    d = fs.read()
    if d == "" or d == "\n":
        curCat=0
    else:
        curCat = int(d)
num=0


only = down()
with open("../config/urls","r") as fs:
    curImg = 0
    while True:
        curThread = threading.active_count() - 1
        if curThread < 10:
            lines = fs.readline()
            try:
                datas = json.loads(lines)
            except Exception:
                continue

            title = datas['title']
            pics = datas['pics']
            ntitle = only.filter(title)

            if ntitle == False:
                continue



            obj = down()
            obj.setParam(ntitle,pics,curImg)
            maxThread  = obj.start()
            exit
            '''
            with open("../config/down_record","a+") as record:
                record.write(ntitle  + ":" + i + "\n")
            '''
            curImg +=1
        else:
            time.sleep(10)




