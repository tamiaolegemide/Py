#!/usr/bin/python3
from abc import ABCMeta,abstractmethod
class interface(object):
    __metaclass__ = ABCMeta #指定这是一个抽象类`
    def __init__(self):
        print('这是接口interface的实现')

    @abstractmethod
    def getPageUrl(self,html):
        pass
    @abstractmethod
    def getHtmlUrl(self,html):
        pass
    @abstractmethod
    def getContent(self,html):
        pass
