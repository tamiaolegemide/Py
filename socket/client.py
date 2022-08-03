#!/usr/bin/python3
import socket,sys
def socket_client():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("127.0.0.1",8080))
    
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    while True:
        data = input("please.input work:").encode()
        s.send(data)
        print("aa",s.recv(1024))
        if data =="exit":
            break
    s.close()

socket_client()
