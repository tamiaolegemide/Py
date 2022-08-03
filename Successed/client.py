#!/usr/bin/python3.7
import socket
import json

def send(url,dirname,filename):
    HOST = '127.0.0.1'  # 服务器的主机名或者 IP 地址
    PORT = 65412 # 服务器使用的端口
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        rs = json.dumps({'url':url,"dirname":dirname,"name":filename})
        s.sendall(rs.encode())
        data = s.recv(1024)

def finish():
    HOST = '127.0.0.1'  # 服务器的主机名或者 IP 地址
    PORT = 65412 # 服务器使用的端口
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        rs = json.dumps("exit")
        s.sendall(rs.encode())
        data = s.recv(1024)
send("http://10.166.146.6:8080/public/static/vip/img/menu_logo.png","fuck",1)
finish()
