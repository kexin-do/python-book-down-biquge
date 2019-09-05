# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:52:06 2018

@author: root
"""
from time import ctime
import time

if __name__=='__main__':
    with open('D:/hello.txt','a',encoding='utf-8') as wt:
        wt.write(time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime())+'saddddddddddd\n');
    
    wt.close();
    with open('D:/hello.txt','r',encoding='GBK',errors='ignore') as hello:
        msg = hello.read();
        print(msg);
    hello.close();