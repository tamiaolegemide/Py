#!/usr/bin/python3.8  
import re
import json
import socket
import os
import time
import asyncio
from urllib import request


if os.path.exists("../config/down_pid") is False:
    with open("../config/down_pid","w+") as fs:
        fs.write("")
        fs.close()
if os.path.exists("../config/down_record") is False:
    with open("../config/down_record","w+") as fs:
        fs.write("")
        fs.close()

while True:
    if os.path.exists("../config/down_check") is False:
        with open("../config/down_check","w+") as fs:
            fs.write("[]")
            fs.close()

    #strtmp = os.popen("ps axu|grep '/usr/bin/python3.7 ./url_get.py'")
    strtmp = os.popen("wc -l ../config/down_record")
    cmdback = strtmp.readlines()

    with open("../config/down_check","r") as fs:
        rs = fs.read()
        fs.close()
    if cmdback == json.loads(rs):
        with open("../config/down_pid","r") as fs:
            pid = fs.read()
            os.popen("kill "+ pid)
            os.popen("setsid python3.8 down.py")

    else:
        with open("../config/down_check","w") as fs:
            fs.write(json.dumps(cmdback))
            fs.close()

    time.sleep(10)




    


                                   
