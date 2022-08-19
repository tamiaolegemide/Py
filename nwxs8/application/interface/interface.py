#!/usr/bin/python3
from abc import ABCMeta,abstractmethod
class interface(object):
    __metaclass__ = ABCMeta #指定这是一个抽象类`

    def find(self,html,preg):
        rs = re.findall(preg,html);
        return rs

    def getPageUrl(self):
        pass

    def getHtmlUrl(self,html):
        pass

    def getContent(self,html):
        pass
