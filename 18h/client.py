#!/usr/bin/python3.7
import asyncio
from pathlib import Path
from urllib import request
import re
import os
import json
import socket

host = "127.0.0.1"
port = 64456

def send(command):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect((host,port))
        sock.sendall(command.encode())
        rs = sock.recv(655650)
        sock.close()
        return rs.decode()

#rs = send(json.dumps({'command':'set',"data":{"url":"https://18h.animezilla.com/manga/3741","page":8}}))
rs = send(json.dumps({'command':'list'}))
rs = json.loads(rs)
n =0
for i in rs:
    n+=1
    if n>20:
        break
    print(rs[i])
