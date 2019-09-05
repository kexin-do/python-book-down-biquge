#coding:utf-8
import tkinter as Tkinter
import threading
import time
from PIL import ImageTk,Image
 
 
 
def count(i):
     for k in range(1, 100+1):
        #text.insert(Tkinter.END,'第'+str(i)+'线程count:  '+str(k)+'\n')
        print('123')
        time.sleep(3)
          
 
def fun():
    for i in range(1, 5+1):
        th=threading.Thread(target=count,args=(i,))
        th.setDaemon(True)#守护线程
        th.start()
    var.set('MDZZ')
 
 
 
root=Tkinter.Tk()
root.title('九日王朝')  #窗口标题
root.geometry('+600+100')#窗口呈现位置
button=Tkinter.Button(root,text='屠龙宝刀 点击就送',font=('微软雅黑',10),command=fun)
button.grid()
var=Tkinter.StringVar()#设置变量
label=Tkinter.Label(root,font=('微软雅黑',10),fg='red',textvariable=var)
label.grid()
print('222')
var.set('我不断的洗澡，油腻的师姐在哪里')
root.mainloop()