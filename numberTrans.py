# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:05:38 2018

@author: root
"""

chinese2number = {
            '零':0,
            '一':1,
            '二':2,
            '三':3,
            '四':4,
            '五':5,
            '六':6,
            '七':7,
            '八':8,
            '九':9,
            '十':10,
            '百':100,
            '千':1000,
            '万':10000
        }

def str2number(chineseNumber):
    
    multi_num_list = []
    temp = 1;
    for i in chineseNumber:
        number = chinese2number.get(i);
        if number == None:
            print('不支持该数字转换')
            multi_num_list.clear()
            multi_num_list.append(-1)
            break
        if number == 10000:
            for j in range(len(multi_num_list)):
                multi_num_list[j] = multi_num_list[j] * number
        if number > 9:
            temp = temp*number
            multi_num_list.append(temp)
        elif number < 1:
            temp=1
        else:
            temp = number
    if temp%10 == 0:
        temp = 0
    for k in multi_num_list:
        temp = temp + k;
    
    return temp
            
if __name__ == '__main__':
    num = 87
    some = int(num/10)
    print(some)
    
    
    
    
    
    
    
    
    
    
    
    
    
    