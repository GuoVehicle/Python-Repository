#coding:utf-8

#1.---字符串操作
# city=input("pleasehhhhsd :")
# url='http://apistore.baidu.com/microservice/weather?citypinyin={}'.format(city)
# print(url)
# num=1
# string='1'
# num2=int(string)
# word='friends'
# search='end'
# print(word[(int(word.find(search))):])
# find_the_evial_in_yours=word[0]+word[2:6]
# print(find_the_evial_in_yours)
# print(num+num2)
# print('{} shi  sb'.format('靳晓楠'))


#2.简单函数操作

#2.1华氏温度转换
# def Fahrenheit_convert(c):
#     fahrenheit=c*9/5+32
#     print(str(fahrenheit)+'`F')
#     return fahrenheit
# c2f=Fahrenheit_convert(35)
# print(c2f)

#2.2重量转换器
# def gconvertkg(c):
#     nog=int(c.find('g'))
#     if(nog>=0):
#         # g=c[:int(c.find('g'))]  --第一种截取方法
#         g = c.replace(c[nog], '')  # --第二种
#         kg = int(g) / 1000
#     else:
#         kg='Incorrect input '
#     return kg
#
# g2kg=input("input please enter g：")
# t=gconvertkg(g2kg)
# print(t)

#2.3求直角三角形斜边长
# def MakeBel(a,b):
#     a=int(a)
#     b=int(b)
#     if isinstance(a,int) and isinstance(b,int):
#         c2 = (abs(a)) ** 2 + (abs(b)) ** 2
#         c=c2**0.5
#     else:
#         c='datatype falseness'
#
#     return c
# a=input('please enter a:')
# b=input('please enter b:')
# print('The right triangle third sides length is  c=',MakeBel(a,b))


# 2.4圣诞树
# print('   *','  ***',' *****','*******','   |   ',sep='\n')


#2.5 在桌面创建一个文件并写入信息 外带敏感词替换后存入

# def Creat_txt_Fiter():
#     name=input('please enter filename:')
#     msg=input('please enter message:')
#     msg=msg.replace('习近平', '郭定康')
#     msg=msg.replace('主席', '大佬')
#     deskop_path=r'C:\Users\Administrator\Desktop\\'
#     full_name=deskop_path+name+'.txt'
#     file=open(full_name,'w')
#     file.write(msg)
#     file.close()
#     print('done!')
#
# Creat_txt_Fiter()

# #2.6 模拟用户初次登陆 修改密码
#
#
# passwordlist=['666666','12345']
# def Account_login():
#     psd=input('please enter password:')
#     passlogin=psd==passwordlist[-1]
#     passret=psd=psd==passwordlist[0]
#     if passlogin:
#         print('login success')
#     elif passret:
#         newpassword=input('please enter new password:')
#         passwordlist.append(newpassword)
#         print('update password success/n')
#         Account_login()
#     else:
#         print('wrong password ')
#         Account_login()
#
# Account_login()


#2.7 乘法口诀表

# for i in range(1,10):
#     for j in range(1,10):
#         #print('{}*{}={}'.format(i,j,i*j))
#         print('%d*%d=%d'%(i,j,i*j))


#2.8 登陆三次密码错误锁定


#2.9 桌面新建10个文件以数字命名

#生成10个文件
# def Create_txt_num():
#     deskop_path=r'C:\Users\Administrator\Desktop\\'
#     for n in range(1,11):
#         full_name=deskop_path+str(n)+'.txt'
#         file=open(full_name,'w')
#         file.write(str(n))
#         file.close()
#         print('file %s  the %s done!'%(full_name,n))
#
# #删除文件
# import os
# def delete_txt_num():
#     deskop_path = r'C:\Users\Administrator\Desktop\\'
#     n=1
#     while n<11:
#         full_namepath=deskop_path+str(n)+'.txt'
#         os.remove(full_namepath)
#         print('delete'+full_namepath+'success')
#         n+=1
# #Create_txt_num()
# delete_txt_num()

#3.0 复利计算函数
# def invest(amount,rate,time):
#
#     all_amount=amount*((1+rate)**time)
#     return all_amount
#
# print(invest(100,0.5,2))

#3.1 打印1-100的偶数
#
# def printEvenNumber():
#     for n in range(1,100):
#         if(n%2==0):
#             print(n)
#         else:
#             pass
#
# printEvenNumber()

#3.2摇骰子游戏 猜大小 加赌注和金额
#
#
#
# #摇骰子函数
# import random
# def roll_dice(number=3,points=None):
#     print('begin  roll dice>>>>>')
#     if points is None:
#         points=[]
#     while number>0:
#         point=random.randrange(1,7)
#         points.append(point)
#         number-=1
#     return points
#
# #根据摇骰子点数计算和判断大小
# def roll_total(nums):
#     isbig=11<=nums<=18
#     issmall=3<=nums<=10
#     if isbig:
#         return 'Big'
#     elif issmall:
#         return 'Small'
#
# #下注金额和赔率
# def money_rate(total_money):
#     money = input('please enter money number:')
#     rate = input('please enter rate:')
#     alls_satake=int(money)*int(rate)
#     if(total_money<alls_satake):
#         print('The lack of the amount')
#         start_game()
#     else:
#         return alls_satake
#
# #开始游戏
# def start_game(total_money=1000):
#     print('start game>>>>')
#     choices=['Big','Small']
#     stake=money_rate(total_money)
#     choice=input('please enter Big or Small:')
#     if choice in choices:
#         points=roll_dice()
#         win=roll_total(sum(points))
#         if choice==win:
#             total_money+=stake
#             print('congratulations on your answer! total is %d , remind money:%d'%(sum(points),total_money))
#             start_game(total_money)
#         else:
#             total_money -= stake
#             print('wrong answer! total is %d, remind money:%d' % (sum(points),total_money))
#             start_game(total_money)
#     else:
#         print('invalid word!!')
#         start_game(total_money)
# start_game()

#3.3 手机号码注册提示
#
# def ver_number():
#     CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184,187, 188, 147, 178, 1705]
#     CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
#     CN_telecom = [133, 153, 180, 181, 189, 177, 1700]
#     number=input('please enter number:')
#     number_rout=int(number[:3])
#     mobile=False
#     union = False
#     telecom = False
#     for n in CN_mobile:
#         if(n==number_rout):
#             mobile=True
#     for n in CN_union:
#         if (n == number_rout):
#             union = True
#     for n in CN_telecom:
#         if (n == number_rout):
#             telecom = True
#     if(len(number)==11):
#         if(mobile or union or telecom):
#             if mobile:
#                 print('Operator:China Mobile /n we are sending ext to your phone:%s'%(number))
#             elif union:
#                 print('Operator:China Union /n we are sending ext to your phone:%s' % (number))
#             elif  telecom:
#                 print('Operator:China Telecom /n we are sending ext to your phone:%s' % (number))
#         else:
#             print('This section does not exist')
#     else:
#         print('invalied be  in 11 degit')
# ver_number()


# #3.4 统计txt文本的单词出现次数
# import string
# def count_txt():
#     path=r'C:\Users\Administrator\Desktop\\'
#     full_filename=path+'Walden.txt'
#     #打开文件
#     with open(full_filename,'r',encoding='utf-8') as file:
#         #文本预处理 小写 无空格  截断装在列表里
#         words=[txt.strip(string.punctuation).lower() for txt in file.read().split()]
#         wordss=set(words)
#         print(wordss)
#         #利用key不可重复  装载单词  value统计个数   字典
#         counts_dict={index:words.count(index) for index in wordss}
#         print(counts_dict)
#     #最后排序输出
#     for word in sorted(counts_dict,key=lambda x:counts_dict[x],reverse=True):
#         print('{}-{}'.format(word,counts_dict[word]))
#
#
# count_txt()


#3.5 类
# class TestA():
#     attr=21
#     def __init__(self):
#         self.attr=32
# obj_a=TestA()
# obj_b=TestA()
# obj_a.attr=33
# print(TestA.__dict__)
# print(obj_a.__dict__)
# print(obj_b.attr)
# print(obj_a.attr)

import sys
print(sys.path[3])
