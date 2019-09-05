# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 10:33:48 2018

@author: self.root
"""

import tkinter as tk
from urllib.parse import quote
import string,requests,book,threadTest,threading,tkinter.messagebox 
from bs4 import BeautifulSoup
from time import sleep


header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'www.biquge.com.tw',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

class MainFrame:

    
    def search(self):
        searchkey = self.get_search_text()
        
        searchkey = searchkey.encode('gbk')
        searchkey = quote(searchkey,safe=string.printable)
        #print(searchkey)
        self.make_table(searchkey)
        
    def get_content_info(self,searchKey,page = 1):
        try:
            request = requests.get('http://www.biquge.com.tw/modules/article/soshu.php?searchkey=+'+searchKey+"&page="+str(page),timeout=15)
            request.encoding = self.encoding
        except BaseException:
            self.show_msg('请求超时')
            
        return request.text
        
    def get_total_page(self,searchKey):
        html = self.get_content_info(searchKey,page=1)
        search_page = BeautifulSoup(str(html),'html5lib')
        page_target = search_page.find_all(class_='last')
        if len(page_target) == 1:
            total_page = int(page_target[0].string)
            return total_page
        return None#找到详细的书目
    '''
        没有找到相关信息提示
    '''
    def show_msg(self,msg):
        self.label_book_search['text'] = msg
    
    
    '''
        加载所有搜索结果
    '''
    def make_list(self, searchKey, total_page):
        odd_list = []
        even_list = []
        for i in range(total_page):
            html = self.get_content_info(searchKey, page=i+1)
        
            odds = BeautifulSoup(str(html),'html5lib').find_all(class_='odd')
            evens = BeautifulSoup(str(html),'html5lib').find_all(class_='even')
            odd_list.extend(odds)
            even_list.extend(evens)
        return (odd_list,even_list)
    
    def find_one_book(self,searchKey):
        html = self.get_content_info(searchKey,page=1)
        metas = BeautifulSoup(str(html),'html5lib').find_all('meta')
        
        single_book = book.Book()
        single_book.author = metas[12]['content']
        print(single_book.author)
        single_book.book_name = metas[13]['content']
        single_book.target = metas[15]['content']
        single_book.status = metas[16]['content']
        single_book.time = metas[17]['content']
        single_book.new_chapter = metas[18]['content']
        single_book.words = '未知'
        
        self.books.append(single_book)
        
        self.btn_book_down_1 = tk.Button(self.root, text = "下载")
        self.btn_book_down_1.grid(row=3,column=7)
        self.btn_book_down_1['width'] = 8
        
        self.make_page_info(0,1)
        
        
        
    
    def make_table(self,searchKey):
        
        total_page = self.get_total_page(searchKey)
        if total_page == None:
            self.find_one_book(searchKey)
        else : 
            (odds,evens) = self.make_list(searchKey,total_page)
            if len(odds) == 0:
                self.show_msg('未找到任何相关信息')
            else:
                self.make_books(odds,evens)
                
                self.make_page_btn()
                
                self.create_down_btn()
                
                self.make_page_info(0,self.one_page_book)
        
        
    def make_page_info(self, start, end):
        
        
        for i in range(start, end):
            book = self.books[i]
            self.create_label(i+3-start,book.book_name,book.new_chapter,book.author,book.words,book.time,book.status,book.target,book)
        
    '''
        创建下载按钮
    '''
    def create_down_btn(self):
        self.btn_book_down_1 = tk.Button(self.root, text = "下载")
        self.btn_book_down_1.grid(row=3,column=7)
        self.btn_book_down_1['width'] = 8
        
        self.btn_book_down_2 = tk.Button(self.root, text = "下载")
        self.btn_book_down_2.grid(row=4,column=7)
        self.btn_book_down_2['width'] = 8
        
        self.btn_book_down_3 = tk.Button(self.root, text = "下载")
        self.btn_book_down_3.grid(row=5,column=7)
        self.btn_book_down_3['width'] = 8
        
        self.btn_book_down_4 = tk.Button(self.root, text = "下载")
        self.btn_book_down_4.grid(row=6,column=7)
        self.btn_book_down_4['width'] = 8
        
        self.btn_book_down_5 = tk.Button(self.root, text = "下载")
        self.btn_book_down_5.grid(row=7,column=7)
        self.btn_book_down_5['width'] = 8
        
        self.btn_book_down_6 = tk.Button(self.root, text = "下载")
        self.btn_book_down_6.grid(row=8,column=7)
        self.btn_book_down_6['width'] = 8
        
        self.btn_book_down_7 = tk.Button(self.root, text = "下载")
        self.btn_book_down_7.grid(row=9,column=7)
        self.btn_book_down_7['width'] = 8
        
        self.btn_book_down_8 = tk.Button(self.root, text = "下载")
        self.btn_book_down_8.grid(row=10,column=7)
        self.btn_book_down_8['width'] = 8
        
        self.btn_book_down_9 = tk.Button(self.root, text = "下载")
        self.btn_book_down_9.grid(row=11,column=7)
        self.btn_book_down_9['width'] = 8
        
        self.btn_book_down_10 = tk.Button(self.root, text = "下载")
        self.btn_book_down_10.grid(row=12,column=7)
        self.btn_book_down_10['width'] = 8
        
        self.btn_book_down_11 = tk.Button(self.root, text = "下载")
        self.btn_book_down_11.grid(row=13,column=7)
        self.btn_book_down_11['width'] = 8
        
        self.btn_book_down_12 = tk.Button(self.root, text = "下载")
        self.btn_book_down_12.grid(row=14,column=7)
        self.btn_book_down_12['width'] = 8
        
        self.btn_book_down_13 = tk.Button(self.root, text = "下载")
        self.btn_book_down_13.grid(row=15,column=7)
        self.btn_book_down_13['width'] = 8
        
        self.btn_book_down_14 = tk.Button(self.root, text = "下载")
        self.btn_book_down_14.grid(row=16,column=7)
        self.btn_book_down_14['width'] = 8
        
        self.btn_book_down_15 = tk.Button(self.root, text = "下载")
        self.btn_book_down_15.grid(row=17,column=7)
        self.btn_book_down_15['width'] = 8
        
    
    def make_page_btn(self):
        total_book = len(self.books)
        
        self.total_page = int(total_book/self.one_page_book) if total_book % self.one_page_book == 0 else int(total_book/self.one_page_book) + 1
        self.current_page = 1
        self.page_btn_first = tk.Button(self.root,text = '1',command=lambda:self.go_to_page('first'))
        self.page_btn_first.grid(row=19,column=1)
        
        self.page_btn_middle = tk.Button(self.root,text = '2',command=lambda:self.go_to_page('middle'))
        self.page_btn_middle.grid(row=19,column=2)
        
        self.page_btn_last = tk.Button(self.root,text = '3',command=lambda:self.go_to_page('last'))
        self.page_btn_last.grid(row=19,column=3)
            
            
    def go_to_page(self,loc):
        current_page_tmp = 0
        if loc == 'last':
            current_page_tmp = int(self.page_btn_last['text'])
        elif loc == 'first':
            current_page_tmp = int(self.page_btn_first['text'])
        else:
            current_page_tmp = int(self.page_btn_middle['text'])
        
        if(self.current_page != current_page_tmp):
            
            if current_page_tmp > 1 and current_page_tmp <self.total_page:
                self.page_btn_first['text'] = str(int(current_page_tmp - 1))
                self.page_btn_middle['text'] = str(int(current_page_tmp))
                self.page_btn_last['text'] = str(int(current_page_tmp + 1))
                
               
            self.current_page = current_page_tmp
            self.create_down_btn()
            self.make_page_info((self.current_page-1)*self.one_page_book,self.current_page*self.one_page_book)
            
        
    def make_books(self,odds,evens):
        self.books.clear()
        current_book = book.Book()
        total = len(odds)
        for i in range(total):
            odd = odds[i]
            even = evens[i]
            if i%3 == 0:
                name_a_s = BeautifulSoup(str(odd),'html5lib').find_all('a')
                current_book.target = name_a_s[0].get('href')
                current_book.book_name = name_a_s[0].string
                chapter_a_s = BeautifulSoup(str(even),'html5lib').find_all('a')
                current_book.new_chapter = chapter_a_s[0].string
            if i%3 == 1:
                current_book.author = odd.string
                current_book.words = even.string
            if i%3 == 2:
                current_book.time = odd.string
                current_book.status = even.string
                self.books.append(current_book)
                current_book = book.Book()
        
        self.show_msg('共找到'+str(len(self.books))+'本书')
        print('共找到',len(self.books),'本书')
        
    def get_search_text(self):
        return self.entry_search.get()
    
    
    def create_label(self,row_num,name,chapter,author,words,time,status,downUrl,book):
        label_book_name = tk.Label(self.root, text = name)
        label_book_name.grid(row=row_num,column=1)
        label_book_name['width'] = 20
        
        label_book_chapter = tk.Label(self.root, text = chapter)
        label_book_chapter.grid(row=row_num,column=2)
        label_book_chapter['width'] = 30
        
        label_book_author = tk.Label(self.root, text = author)
        label_book_author.grid(row=row_num,column=3)
        label_book_author['width'] = 10
        
        label_book_words = tk.Label(self.root, text = words)
        label_book_words.grid(row=row_num,column=4)
        label_book_words['width'] = 10
        
        label_book_time = tk.Label(self.root, text = time)
        label_book_time.grid(row=row_num,column=5)
        label_book_time['width'] = 15
        
        label_book_status = tk.Label(self.root, text = status)
        label_book_status.grid(row=row_num,column=6)
        label_book_status['width'] = 8
        
        if row_num == 3:
            self.btn_book_down_1['command'] = lambda : self.down(downUrl,self.btn_book_down_1,book)
            self.changeState(self.btn_book_down_1,book)
        elif row_num == 4:
            self.btn_book_down_2['command'] = lambda : self.down(downUrl,self.btn_book_down_2,book)
            self.changeState(self.btn_book_down_2,book)
        elif row_num == 5:
            self.btn_book_down_3['command'] = lambda : self.down(downUrl,self.btn_book_down_3,book)
            self.changeState(self.btn_book_down_3,book)
        elif row_num == 6:
            self.btn_book_down_4['command'] = lambda : self.down(downUrl,self.btn_book_down_4,book)
            self.changeState(self.btn_book_down_4,book)
        elif row_num == 7:
            self.btn_book_down_5['command'] = lambda : self.down(downUrl,self.btn_book_down_5,book)
            self.changeState(self.btn_book_down_5,book)
        elif row_num == 8:
            self.btn_book_down_6['command'] = lambda : self.down(downUrl,self.btn_book_down_6,book)
            self.changeState(self.btn_book_down_6,book)
        elif row_num == 9:
            self.btn_book_down_7['command'] = lambda : self.down(downUrl,self.btn_book_down_7,book)
            self.changeState(self.btn_book_down_7,book)
        elif row_num == 10:
            self.btn_book_down_8['command'] = lambda : self.down(downUrl,self.btn_book_down_8,book)
            self.changeState(self.btn_book_down_8,book)
        elif row_num == 11:
            self.btn_book_down_9['command'] = lambda : self.down(downUrl,self.btn_book_down_9,book)
            self.changeState(self.btn_book_down_9,book)
        elif row_num == 12:
            self.btn_book_down_10['command'] = lambda : self.down(downUrl,self.btn_book_down_10,book)
            self.changeState(self.btn_book_down_10,book)
        elif row_num == 13:
            self.btn_book_down_11['command'] = lambda : self.down(downUrl,self.btn_book_down_11,book)
            self.changeState(self.btn_book_down_11,book)
        elif row_num == 14:
            self.btn_book_down_12['command'] = lambda : self.down(downUrl,self.btn_book_down_12,book)
            self.changeState(self.btn_book_down_12,book)
        elif row_num == 15:
            self.btn_book_down_13['command'] = lambda : self.down(downUrl,self.btn_book_down_13,book)
            self.changeState(self.btn_book_down_13,book)
        elif row_num == 16:
            self.btn_book_down_14['command'] = lambda : self.down(downUrl,self.btn_book_down_14,book)
            self.changeState(self.btn_book_down_14,book)
        elif row_num == 17:
            self.btn_book_down_15['command'] = lambda : self.down(downUrl,self.btn_book_down_15,book)
            self.changeState(self.btn_book_down_15,book)
    
    def changeState(self, btn, book):
        if book.state == 0:
            btn['text'] = '下载'
        elif book.state == 1:
            btn['text'] = '下载中'
            btn['state'] = 'disable'
        else:
            btn['text'] = '已完成'
            btn['state'] = 'disable'
    '''
        为每个任务开启新的线程，避免界面阻塞不能点击
    '''
    def down(self, url, btn, current_book):
        btn.configure(state='disable')
        btn['text'] = '下载中'
        current_book.state = 1
        tt = threadTest.ThreadTest(url)
        th=threading.Thread(target=tt.down,name=url)
        
        self.work_queue[url] = th
        th.setDaemon(True)#守护线程
        th.start()
        
        
    def check_work_state(self):
        while True:
            for key in list(self.work_queue.keys()):
                sleep(2)
                if self.work_queue[key].is_alive() == False:
                    print('线程执行完毕，更新书状态')
                    book_url = self.work_queue[key].getName()
                    for this_book in self.books:
                        if this_book.target == book_url:
                            this_book.state = 2
                            del self.work_queue[key]
                            tkinter.messagebox.showinfo("系统提示","书《"+this_book.book_name+"》已下载完成")
                            break
                        
        
    def __init__(self,encoding='utf-8'):
        self.one_page_book = 15
        self.encoding = encoding
        self.books = []
        self.root = tk.Tk()
        self.root.title('偷书小哥')
        self.root.geometry("800x600")
        self.work_queue = {}
        self.base_url = 'http://www.biquge.com.tw/modules/article/soshu.php'
        self.entry_search = tk.Entry(self.root)
        self.entry_search.grid(row = 0, column = 1,columnspan=5,sticky=tk.W)
        self.entry_search['width'] = 90
        self.btn_search = tk.Button(self.root, text = "搜索",command=self.search)
        self.btn_search.grid(row = 0, column = 7)
        self.btn_search['width'] = 5
        
        self.label_book_search = tk.Label(self.root)
        self.label_book_search.grid(row=1,columnspan=8)
        
        check_thread = threading.Thread(target=self.check_work_state)
        check_thread.setDaemon(True)
        check_thread.start()
        
        label_book_name = tk.Label(self.root, text = "书名")
        label_book_name.grid(row=2,column=1)
        label_book_name['width'] = 20
        
        label_book_chapter = tk.Label(self.root, text = "最新章节")
        label_book_chapter.grid(row=2,column=2)
        label_book_chapter['width'] = 30
        
        label_book_author = tk.Label(self.root, text = "作者")
        label_book_author.grid(row=2,column=3)
        label_book_author['width'] = 10
        
        label_book_words = tk.Label(self.root, text = "字数")
        label_book_words.grid(row=2,column=4)
        label_book_words['width'] = 10
        
        label_book_time = tk.Label(self.root, text = "更新")
        label_book_time.grid(row=2,column=5)
        label_book_time['width'] = 15
        
        label_book_status = tk.Label(self.root, text = "状态")
        label_book_status.grid(row=2,column=6)
        label_book_status['width'] = 8
        
        label_book_down = tk.Label(self.root, text = "下载")
        label_book_down.grid(row=2,column=7)
        label_book_down['width'] = 8
        
        
        
        self.root.mainloop()
  

if __name__=='__main__':
    win = MainFrame('GBK')



