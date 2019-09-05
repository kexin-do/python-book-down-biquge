# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 10:59:56 2018

@author: root
"""

import threading,workTool,sys
from time import sleep,ctime


class ThreadTest:
    
    def run(self,wt, start, end):
        urls = wt.urls
        names = wt.names
        for i in range(start, end):
            name = names[i]
            sleep(1)
            try:
                wt.set_book_text(i,wt.get_content(urls[i]))
                sys.stdout.write('\r已加载 %.1f%%  ' % float((((len(workTool.contents))/wt.chapter_nums)*100)))
                sys.stdout.flush()
            except BaseException:
                self._exceptions_[i] = urls[i]
                print(name,'已进入重新请求队列','共',len(self._exceptions_),'章')
                continue
                
    def __init__(self,target):
        
        self.target = target
        self._exceptions_ = {}
        self._threads_ = []
    
    def down_book_by_threadings(self,wt,numberOfWorkToRunByThread,total):
        all_thread = 1 if int(total/numberOfWorkToRunByThread) == 0 else int(((total/numberOfWorkToRunByThread)+0.5))
        print('共有',all_thread,'个爬虫在工作，平均每个爬取',numberOfWorkToRunByThread,'条数据')
        some = 1
        if(all_thread != 1):
             some = int(((total/all_thread)+0.5))
        for i in range(all_thread):
            
            if(i!=all_thread-1):
                current_thread = threading.Thread(target=self.run,name='down'+str(i),args=(wt,some*i,some*(i+1)))
            else:
                current_thread = threading.Thread(target=self.run,name='down'+str(i),args=(wt,some*i,total))
            self._threads_.append(current_thread)
    
    
    def down(self):
        down_book = workTool.WorkTool(self.target,'gbk');
        down_book.get_down_url()
        total = down_book.chapter_nums
        self.down_book_by_threadings(down_book, 25, total)
        
        for t in self._threads_:
            t.setDaemon(True);
            t.start();
        for t in self._threads_:
            t.join();
        
        ex_len = len(self._exceptions_)
        print('开始加载未完成的章节...,共',ex_len,'章')
        print(list(self._exceptions_.keys()))
        while True:
            if len(self._exceptions_) == 0:
                print('处理完成...')
                break;
            
            for key in list(self._exceptions_.keys()):
                url = self._exceptions_.get(key)
                try:
                        
                    down_book.set_book_text(key,down_book.get_content(url))
                    sys.stdout.write('\r剩余 %d 章  ' % len(self._exceptions_))
                    sys.stdout.flush()
                    del self._exceptions_[key]
                except BaseException:
                    continue
        print('加载完成')
        print('总大小：',len(workTool.contents))
        down_book.down()
        
            
        print("done! ", ctime());
