#!/usr/bin/python3.7
import asyncio
from pathlib import Path
from urllib import request
import re
import os
import json

'''
async def fuck(num):
    await asyncio.sleep(num)
    print(num)

async def main():
    task1 = asyncio.create_task(fuck(1))
    task2 = asyncio.create_task(fuck(1))
    await task1
    await task2



asyncio.run(main())

'''

import socket

HOST = '127.0.0.1'  # 标准的回环地址 (localhost)
PORT = 65412        # 监听的端口 (非系统级的端口: 大于 1023)


class down:
    def add(self,dirname,url,name=False,headers={}):
        dirname = dirname.replace("/","-")
        rs = os.path.exists("./"+dirname)
        if rs == False:
            os.mkdir(dirname)
        req = request.Request(url,headers=headers)
        recv = request.urlopen(req)
        
        groups = re.search("\.(.{1,4})$",url)
        if groups:
            suf = groups.group(1)

        if name:
            filename = str(name) + "." + suf
        else:
            groups = url.split("/")
            filename = groups[len(groups)-1]

        fs = open("./"+dirname+"/"+filename,"wb")
        fs.write(recv.read())


        
    def addError(self,name,value):
        print(name,value)
        print("error")

#f = down()
#f.add("fuck","https://img.alicdn.com/tfs/TB12k3rUXzqK1RjSZFCXXbbxVXa-108-108.png",3)
async def newObj(conn):
    obj = down()
    while True:
        data = conn.recv(1024)
        data = json.loads(data)
        if data == "exit":
            return False
        else:
            obj.add(data["dirname"],data["url"],data["name"],data['headers'])
        return data



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    arr = []
    while True:
        conn, addr = s.accept()
        with conn:
            rs = asyncio.run(newObj(conn))
            arr.append(rs)
            if rs == False:
                conn.close()
                break

