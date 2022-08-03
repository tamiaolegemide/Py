#!/usr/bin/python3.7
import re
import json
import socket
import os
import time
import asyncio
from urllib import request



while True:
    #strtmp = os.popen("ps axu|grep '/usr/bin/python3.7 ./url_get.py'")
    strtmp = os.popen("ps axu|grep '/usr/bin/python3.7 ./18h.py'")
    cmdback = strtmp.readlines()
    if len(cmdback) <  3:
        os.popen("nohup ./18h.py > error&")
    time.sleep(1)

