#!/usr/bin/python3
import re,json,os,asyncio,time,datetime,threading,shutil
from urllib import request
from interface import interface

class filter(interface.interface):
    recordUrl = "../data/record"
    downLoadUrl = "../Download"
    txtUrl = "../Txt"
    maxThread = 10
    #while maxThread > 0:


    def getPageUrl(self,content):
        pass

    def getHtmlUrl(self,content):
        pass

    def getContent(self,html):
        pass


    

