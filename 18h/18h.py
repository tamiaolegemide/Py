#!/usr/bin/python3.7
import re,json,socket,os,asyncio,time,datetime,threading
from urllib import request

arr = {}






class download(threading.Thread):
    urls = {}
    host = "127.0.0.1"
    port = 64460
    maxThread = 10

    def sendHttp(self,url):
        req = request.Request(url)
        p = request.urlopen(req)
        return  p.read().decode()

    def sendCommand(self,command,data):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
            id = threading.get_ident()
            sock.connect((self.host,self.port))
            rs = {"id":id,"command":command,"data":data}
            #print("client_send",rs)
            sock.sendall(json.dumps(rs).encode())
            rs = sock.recv(2048)
            #print("server:",rs)
            sock.close()
            if rs is not "":
                return json.loads(rs)


    def getMax(self):
        return self.maxThread

    def run(self):
        rs = self.getTask()
        if "command" in rs:
            if rs["command"] == "exit":
                self.maxThread -=1
                return True
            elif rs['command'] == "task":
                data = rs['data']
                url = data['u']
                cur = data['c']
                self.getManagePage(url,cur)
        return self.maxThread

    def getTask(self):
        task  = self.sendCommand("get","")
        self.loadRs(task)
        return task


    def loadRs(rs):
        if rs is "":
            return True
        command = rs['command']
        data = rs['data']
        if command == "sleep":
            time.sleep(data)
        




    def getManagePage(self,manga_url,cur = 0):
        content = self.sendHttp(manga_url)
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
        maxPage +=1

        img_src = re.search("<img id=\"comic\" class=\"loading\".*?src=\"(.*?)\">",content)
        img_src = img_src.group(1)

        #send(img_src,title,1)
        cur+=1
        for i in range(cur,maxPage):
            next_url = manga_url+"/"+str(i+1)
            content = self.sendHttp(next_url)
            img_src = re.search("<img id=\"comic\" class=\"loading\".*?src=\"(.*?)\">",content)
            img_src = img_src.group(1)
            self.send(img_src,title,int(i))
            rs = self.sendCommand("set",{"u":manga_url,"c":i})
            self.loadRs(rs)
        rs = self.sendCommand("end",{"u":manga_url})
        self.loadRs(rs)
        return True



    def send(self,url,dirname,name):
        dirname = dirname.replace("/","-")
        #print(dirname,threading.get_ident())
        rs = os.path.exists("./"+dirname)
        if rs == False:
            os.mkdir(dirname)

        groups = re.search("\.(.{1,4})$",url)
        if groups:
            suf = groups.group(1)

        if name:
            filename = str(name) + "." + suf
        else:
            groups = url.split("/")
            filename = groups[len(groups)-1]

        isfile = os.path.isfile("./"+dirname+"/"+filename)
        if isfile is True:
            return True

        fs = open("result","a+")
        fs.write(url+" | " + dirname + " | " + str(name) +"\n")
        fs.close()


        headers={"Referer":"http://18h.animezilla.com"}
        req = request.Request(url,headers=headers)
        recv = request.urlopen(req)


        fs = open("./"+dirname+"/"+filename,"wb")
        fs.write(recv.read())
        fs.close()
        return True


maxThread = 10
#while maxThread > 0:
while True:
    curThread = threading.active_count() - 1
    if curThread < 10:
        obj = download()
        maxThread  = obj.start()
        maxThread  = obj.getMax()
    else:
        pass
    time.sleep(1)
print("download finish")




