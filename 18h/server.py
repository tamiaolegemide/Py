#!/usr/bin/python3.7
import asyncio
from pathlib import Path
from urllib import request
import re ,os ,json ,socket ,time



class server :
    maxThread = 10
    host = "127.0.0.1"
    port = 64460
    data = {}
    threads = {}

    def checkThreads(self):
        for i in self.threads:
            if time.time() - self.threads[i] > 120 :
                self.threads.pop(i)

    def checkTime(self):
        subtime = time.time() - self.startTime
        if subtime >= 60 * 30:
            return True
        else:
            return False

    def tosleep(self,n):
        self.send("sleep",10)




    def initData(self):
        with open("url","r") as fs:
            urls = fs.readlines()
            n = 0
            for i in urls :
                i = i.replace("\n","")
                curThread  = n % self.maxThread
                if curThread in self.data:
                    self.data[curThread].append({
                            's' : 0,
                            'c' : 0,
                            't' : time.time(),
                            'u' : i,
                            })
                else:
                    self.data[curThread] =[]
                n+=1
            fs.close()

    def checkDatas(self):
        if self.checkTime():
            self
            temp = []
            for thread in self.data:
                for data in thread:
                    if data['s'] == 0:
                        temp.append(data['u'])
            n = 0
            for i in temp:
                i = i.replace("\n","")
                curThread  = n % self.maxThread
                if curThread in self.data:
                    self.data[curThread].append({
                            's' : 0,
                            'c' : 0,
                            't' : time.time(),
                            'u' : i,
                            })
                else:
                    self.data[curThread] =[]
                n+=1
            fs.close()





    def reg(self,id):
        self.threads[id] = time.time()

    def logout(self,id):
        if id in self.threads:
            self.threads.pop(id)


#get , list ,set ,exit ,end
    def command(self,id,command,data):
        self.reg(id)
        self.checkDatas() #整理数据
        curNum = self.getNum(id)
        self.checkData(curNum) #检查过期数据
        if curNum is False:
            return False
        if command == "get":
            self.getUrl(curNum)
        if command == "set":
            self.setProgress(curNum,data['u'],data['c'])
        if command == "end":
            self.markEnd(curNum,data['u'])
        if command == "exit":
            pass
        if command == "list":
            self.getList(curNum)
    def getList(self,curThread):
        if curThread in self.data:
            self.send("list",self.data[curThread])

    def markEnd(self,curThread,url):
        if curThread in self.data:
            data = self.data[curThread]
            for i in data:
                if i['u'] == url:
                    i['s'] = 2
                    i['t'] = time.time()
            self.data[curThread] = data
        else:
            print("markEnd : no curThread :" + curThread + "\n")
        self.send("ok","")

    def getUrl(self,curNum):
        if curNum in self.data:
            curData = self.data[curNum]
            isEnd = True
            for i in curData:
                if i['s'] == 0:
                    isEnd = False
                    self.send("task",{"u":i['u'],"c":i['c']})
                    break
            if isEnd is True:
                    self.send("exit","")


    def setProgress(self,curThread,url,curPage):
        if curThread in self.data:
            data = self.data[curThread]
            for i in data:
                if i['u'] == url:
                    i['s'] = 1
                    i['t'] = time.time()
                    i['c'] = curPage
            self.data[curThread] = data
        self.send("ok","")



    def checkData(self,curNum):
        if curNum in self.data:
            self.tosleep(10)
            curData = self.data[curNum]
            for i in curData:
                curTime = time.time()
                if ((curTime - i['t']) > 60) and (i['s'] == 1):
                    i['s'] = 0
                    i['t'] = curTime
            self.data[curNum] = curData


    def getNum(self,id):
        n = 0 
        curNum = False
        for i in self.threads:
            if i == id:
                curNum = n
            n+=1
        return curNum
    
    def send(self,command,data):
        rs = {"command":command,"data":data}
        jsonRs = json.dumps(rs).encode()
        self.conn.sendall(jsonRs)

    def __init__(self):
        self.startTime = time.time()
        self.initData()
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as self.sock:
            self.sock.bind((self.host,self.port))
            self.sock.listen()
            isEnd = True
            while True:
                self.conn,self.addr = self.sock.accept()
                content = self.conn.recv(1024)
                content = json.loads(content.decode())
                with open("command","a+") as fs:
                    fs.write(json.dumps(content)+"\n")
                    fs.close()
                self.command(content["id"],content["command"],content["data"])
                self.conn.close()
                time.sleep(0.1)



obj = server()
