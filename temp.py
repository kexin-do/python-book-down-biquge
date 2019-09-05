# -*- coding: utf-8 -*-
"""
    python爬虫基于BeautifulSoup和requests爬取笔趣阁图书
"""
from bs4 import BeautifulSoup
from enum import Enum

import requests, sys

SelectorType = Enum('SelectorType', ('menu', 'book', 'text'))

class downBook:

    
    '''
        构造函数
        参数说明：
            server:请求地址
            target:小说所在请求的目录
            menu_selector:目录ID
            menu_class:只有当menu为None是才取该值
            book_selector:书名id
            book_class:同menu_class
            text_selector:内容id
            text_class:同menu_class
            charset:下载小说网站编码格式
            markup_type:解析html的方式,建议使用html5lib , lxml不能完全获取所有的html标签
    '''
    def __init__(self, server, target, menu_selector, menu_class, book_selector, book_class, text_selector, text_class, charset='utf-8'):
        self.server = server;
        self.target = target;
        self.menu_selector = menu_selector;
        self.menu_class = menu_class;
        self.text_selector = text_selector;
        self.text_class = text_class;
        self.book_selector = book_selector;
        self.book_class = book_class;
        self.charset = charset;
        self.urls = [];
        self.names = [];
        self.book_name = '';
        self.markup_type = 'html5lib';
        self.num = 0;
    '''
        函数说明：通过requests模块获取请求地址的html信息
        参数说明：
            target:目标地址
        返回值：
            获取的html信息
    '''
    def _get_html_(self,target):
        req = requests.get(target);
        req.encoding = self.charset;
        
        return req.text;
    
    '''
        函数说明：通过soup解析传入的html信息，获取相应的标签信息
        参数说明:
            html:html信息通过requests获取
            selector_type:id选择器类型：menu,book,text三种
        返回值：
            通过选择器筛选出的结果
    '''
    def _get_use_soup_(self, html, selector_type):
        this_soup = BeautifulSoup(html, self.markup_type);
        this_type = '';
        is_selector = True;
        if (selector_type==SelectorType.menu):
            this_type = self.menu_selector;
            if(this_type==None):
                is_selector = False;
                this_type = self.menu_class;
        elif (selector_type==SelectorType.book):
            this_type = self.book_selector;
            if(this_type==None):
                is_selector = False;
                this_type = self.book_class;
        elif (selector_type==SelectorType.text):
            this_type = self.text_selector;
            if(this_type==None):
                is_selector = False;
                this_type = self.text_calss
        
        if is_selector:
            return this_soup.find_all(id = this_type);
        else :
            return this_soup.find_all(class_=this_type);

    '''
        函数说明：获取所提供地址信息，获取相应的文本地址信息，标题信息，和总章节数
    '''
    def get_down_url(self):
        html = self._get_html_(self.target)
        
        this_name = self._get_use_soup_(html, SelectorType.book);
        
        book_name_tmp = BeautifulSoup(str(this_name), self.markup_type);
        self.book_name = book_name_tmp.find_all('h1')[0].string;
        
       
        menu = self._get_use_soup_(html, SelectorType.menu);
        target_a_s = BeautifulSoup(str(menu), self.markup_type);
        a_s = target_a_s.find_all('a');
        
        self.num = len(a_s);
        print('正在加载目录');
        for a in a_s:
            self.names.append(a.string);
            self.urls.append(self.server+a.get('href'));
        print(self.num)
        print('目录加载成功');
    '''
        函数说明：获取所提供地址的文本内容
        参数说明：
            url:文本获取地址
        返回值：获取结果
    '''
    def get_content(self, url):
        texts = self._get_use_soup_(self._get_html_(url), SelectorType.text);

        text = texts[0].text.replace('\xa0'*8, '\n\n')
        return text;
    '''
        函数说明：向提供的地址写入一获取的文本信息
        参数说明:
            name:当前章节名称
            saveName:保存地址
            text:文本内容
    '''
    def writer(self):
        with open(down_book.book_name+'.txt', 'a', encoding='utf-8') as textFile:
            for textNum in range(1, down_book.num):
                textFile.write(down_book.names[textNum]+'\n');
                textFile.writelines(self.get_content(down_book.urls[textNum]));
                textFile.write('\n\n');
                sys.stdout.write('  \r已下载 %.1f%%' % float(((textNum+1)/down_book.num)*100) )
                sys.stdout.flush();
        textFile.close()
        
if __name__ == "__main__":
    target = "http://www.biquge.com.tw/14_14055/";
    server = "http://www.biquge.com.tw/";
    down_book = downBook(server, target, 'list', None, 'info', None, 'content', None,'gbk');
    down_book.get_down_url();
    print('开始下载')
    down_book.writer()
    print('\n下载完成')
    
    