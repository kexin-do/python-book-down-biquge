# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:13:31 2018

@author: root
"""

from bs4 import BeautifulSoup
from enum import Enum

import requests,time,sys

selectorType = Enum('selectorType',('book','menu','text'))

contents = {}

class WorkTool:
    
    def __init__(self,target,charset='utf-8'):
        self.server = 'http://www.biquge.com.tw/'
        self.target = target#爬取目标地址
        self.menu_selector = 'list'#目录id
        self.book_selector = 'info'#书名称获取id
        self.text_selector = 'content'#内容的id
        self.markup_type = 'html5lib'#html解析方式
        self.book_name = ''#书名
        self.chapter_nums = 0#该书的章节数
        self.urls = {}#书的url地址
        self.names = {}#书的章节名称
        #self.contents = []#书的章节内容
        self.charset = charset
    
        
    def _get_html_(self, url):
        request = requests.get(url,timeout=5)
        request.encoding = self.charset
        return request.text
    
    
    def print_something(*words):
        print(time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime()), words[1])
    
    def _get_current_soup_(self,html,selector_type):
        #解析获取到的网页
        current_soup = BeautifulSoup(html,self.markup_type)
        current_selector = ''
        if selector_type == selectorType.book:
            current_selector = self.book_selector
            
        elif selector_type == selectorType.menu:
            current_selector = self.menu_selector
            
        elif selector_type == selectorType.text:
            current_selector = self.text_selector

        return current_soup.find_all(id=current_selector)
    
    def _set_book_name_(self,html):
        self.book_name = BeautifulSoup(str(self._get_current_soup_(html,selectorType.book)),self.markup_type).find_all('h1')[0].string
        self.print_something('当前爬取的书名称为：《'+self.book_name+'》')
        
    def _set_book_menu_(self,html):
        target_a_s = BeautifulSoup(str(self._get_current_soup_(html,selectorType.menu)),self.markup_type).find_all('a')
        self.chapter_nums = len(target_a_s);
        self.print_something(' 《'+self.book_name+'》的目录正在加载中...')
        i = 0
        for target_a in target_a_s:
            self.names[i] = target_a.string
            self.urls[i] = self.server+target_a.get('href')
            i = i + 1
        self.print_something(' 《'+self.book_name+'》的目录加载完毕!共'+str(self.chapter_nums)+'章')

    
    def get_content(self, url):
        texts = self._get_current_soup_(self._get_html_(url), selectorType.text)
        
        return texts[0].text.replace('\xa0'*8,'\n\n')
        
    def set_book_text(self,key,text):
        #self.print_something(' 《'+self.book_name+'》的内容正在加载中...')
        #for i in range(self.chapter_nums):
            #self.print_something('正在加载 《'+self.book_name+'》 '+self.names[i]);
            #self.contents.append(self.get_content(self.urls[i]))
        contents[key] = text; 
        #self.print_something(' 《'+self.book_name+'》的内容加载完毕...')
        
    def get_down_url(self):
        html = self._get_html_(self.target)
        self._set_book_name_(html)
        self._set_book_menu_(html)
        #self._set_book_text_()
        
        
    def down(self):
        
        with open(self.book_name+'.txt','a',encoding='utf-8',errors='ignore') as book:
            for textNum in range(self.chapter_nums):
                name = self.names[textNum]
                self.print_something('正在下载 《'+self.book_name+'》 '+name);
                book.write(name+'\n')
                book.writelines(contents[textNum])
                book.write('\n\n')
                sys.stdout.write('  \r已下载 %.1f%%' % float(((textNum+1)/self.chapter_nums)*100) )
                sys.stdout.flush();
        book.close();




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        