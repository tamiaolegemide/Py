#!/usr/bin/python3.8
import random
import re,json,socket,os,asyncio,time,datetime,threading
from urllib import request

arr = {}


class download(threading.Thread):
    n =0 
    maxThread = 10
    u_config = "../config"
    u_urls= u_config + "/urls"
    u_record = u_config + "/record"
    u_result = u_config + "/result"
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
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
            ]

    HEADER = {
            'User-Agent': random.choice(user_agent),  # 浏览器头部
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', # 客户端能够接收的内容类型
            'Accept-Language': 'en-US,en;q=0.5', # 浏览器可接受的语言
            'Connection': 'keep-alive', # 表示是否需要持久连接
            }

    def saveUrl(self,title,ics):
        with open(self.u_urls,"a+") as fs:
            jsons = {'title':title,'pics':ics}
            fs.write(json.dumps(jsons)+"\n")
            fs.close()

    def record(self,content):
        with open(self.u_record,"a+") as fs:
            fs.write(content)
            fs.close()
    def setN(self,n):
        self.n = n

    def __init__(self, n):
        super(download, self).__init__()  # 重构run函数必须要写
        self.n = n

    def run(self):
        i = self.n
        pre = "https://bbs8.my7x9j.live/2048"
        #pre = "https://pw.w00l66.xyz/2048"
        url=pre+"/thread.php?fid-28-page-"+str(i)+".html"
        #url="http://www.baidu.com";
        try:
            req = request.Request(url,headers=self.HEADER)
            p = request.urlopen(req)
        except Exception:
            exit()

        lists = p.read().decode()
        gp = re.findall("read.php\?tid.*?\.html",lists);
        ngp = []



        for z in gp:
            if z not in ngp:
                ngp.append(z)

        for j in ngp:
            ju = re.search("tid-\d*",j)
            if ju.group(0) is not None:
                j = "read.php?"+ju.group(0) + ".html"


            iurl = pre+ "/" +j

            try:
                ireq = request.Request(iurl,headers=self.HEADER)
                p = request.urlopen(ireq)
                icontent = p.read().decode()
            except Exception:
                break;
            with open(self.u_result,"a+") as fs:
                fs.write(iurl+"\n")
                fs.close()
            #print(icontent)
            ics = re.findall('<img src="(.*?jpg|png)"',icontent)
            title = re.search("<title>(.*?)<\/title>",icontent);
            if title == None:
                title = ""
            else:
                title = title.group(1)
            self.saveUrl(title,ics)

    def getMax(self):
        return self.maxThread



maxThread = 10
#while maxThread > 0:

if False == os.path.exists("../config/current"):
    with open("../config/current","w+") as fs:
        fs.write("0")
        fs.close()


with open("../config/current","r") as fs:
    i=fs.read()
    fs.close()
    if i == "" or i == "\n":
        i=0

i=int(i)

with open("../config/pid","w+") as fs:
    pid= os.getpid()
    fs.write(str(pid))
    fs.close()
while True:
    curThread = threading.active_count() - 1
    if curThread < 10:
        i=i+1
        obj = download(i)

        if i>=949:
            exit()
        with open("../config/current","w") as fs:
            fs.write(str(i))
            fs.close()
        obj.start()


    else:
        pass
    time.sleep(1)
