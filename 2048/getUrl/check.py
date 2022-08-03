#!/usr/bin/python3.8  
import re
import json
import socket
import os
import time
import asyncio
from urllib import request



while True:
    if os.path.exists("../config/check") is False:
        with open("../config/check","w+") as fs:
            fs.write("[]")
            fs.close()


    if os.path.exists("../config/urls") is False:
            os.popen("setsid /usr/bin/python3.8 index.py")
            time.sleep(10)
            continue


    #strtmp = os.popen("ps axu|grep '/usr/bin/python3.7 ./url_get.py'")
    strtmp = os.popen("wc -l ../config/urls")
    cmdback = strtmp.readlines()

    with open("../config/check","r") as fs:
        rs = fs.read()
        fs.close()
    if cmdback == json.loads(rs):
        with open("../config/pid","r") as fs:
            pid = fs.read()
            os.popen("kill "+ pid)
            os.popen("setsid /usr/bin/python3.8 index.py")

    else:
        with open("../config/check","w") as fs:
            fs.write(json.dumps(cmdback))
            fs.close()

    time.sleep(10)




    


                                   
