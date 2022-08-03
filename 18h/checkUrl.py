#!/usr/bin/python3.7
import re
import json
import socket
import os
import time
import asyncio
from urllib import request



with open("url","r") as fs:
    urls = fs.readlines()
    fs.close()
with open("command","r") as fs:
    commands = fs.readlines()
    fs.close()

    n = 0
    has = []
    for command in commands:
        rs = re.search("end",command)
        if rs is not None:
            rs = re.search("https://18h.animezilla.com/manga/\d*",command)
            if rs.group(0) not in has:
                has.append(rs.group(0))


    with open("no","a+") as fs:
        for url in urls:
            url = url.replace("\n","")
            if url not in has:
                fs.write(url+"\n")

