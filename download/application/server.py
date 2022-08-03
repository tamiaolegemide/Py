#!/usr/bin/python3
import time ,sys,socket,threading
arr =[11,22,33,44,55,66]
pointer =  0
def deal_data(conn,addr,pointer):
    print("Accept new connection from {0}".format(addr))
    conn.send("Hello world".encode())
    while True:
        data = conn.recv(1024)
        print("{0} client send data is {1}".format(addr,data.decode()))
        time.sleep(1)
        if data == "exit" or not data:
            print("{0} connection close ".format(addr) )
            conn.send(bytes('Connection closed!'),'UTF-8')
            break
        data = arr[pointer]
        conn.send(bytes('Hello,{0}'.format(data),'UTF-8'))
    conn.close()

def socket_service():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #s.setsockopt(socket.SOL_SOCKET,SO_REUSEADDR,1)
        s.bind(('127.0.0.1',8080))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    print('Waiting connection...')

    pointer = 0
    while True:
        conn,addr = s.accept()
        pointer+=1
        t = threading.Thread(target = deal_data,args=(conn,addr,pointer))
        t.start()


if __name__ == '__main__':
    socket_service()

