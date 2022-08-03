#!/usr/bin/python3.7
import threading
import time

rs = threading.active_count()

class Test(threading.Thread):
    def setN(self,n):
        self.n = n

    def fuck(self,i):
        n =0
        while True:
            n+=1
            time.sleep(1)
            print(str(i)+" fuck")
            if n > 5 :
                break
        print(str(i) + " end")

    def run(self):
        sub = 5 - self.n
        self.fuck(i)





while True:

    i = 5
    sub = 6 - threading.active_count()
    for i in range(sub):
        obj = Test()
        obj.setN(i)
        obj.start()
