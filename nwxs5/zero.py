#!/usr/bin/python3.7
import re
import json
import socket
import os
import time
import asyncio

files = os.listdir("./novel") for i in files:
    size=os.path.getsize("./novel/"+i)
    if size == 0:
        print(i)
