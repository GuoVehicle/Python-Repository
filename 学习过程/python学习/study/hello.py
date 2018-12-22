
#-*- coding:utf-8 -*-

#1.分数测试
# name=input('输入你的名字:')
# s1=float(input('输入第一次成绩:'))
# s2=float(input('输入第二次成绩:'))
# t=(s2-s1)*100
# if(t>0):
#     print('%s的成绩上升了%.1f%%' %(name,(t/s2)))
# else:
#     print('%s的成绩下降了%.1f%%' %(name,-(t/s2)))

#2.关于list和tuple
# list=['a','2','3']
# t=('A','B',list)
# list=['a','2','5']
# list[2]=5

# print(t)
#

#3.杨辉三角
# age=20
# if age>6 and age<18:
#     print('今年我%stennge'%age)
# elif age>18 and age>28:
#     print('今年我%schhh'%age)
# else:
#     print('今年我%schhhss'%age)

#4.ifelse
# s=int(input('请输入你的出生年份'))
# if s>2000:
#     print('你是林玲后%f'%s)
# else:
#     print('nishi90后%f'%s)

#5.循环 for...in...  while   break continue  set dict
# name=['guodingkang','hahaha','michael']
# for names in name:
#     print(names)

#     sum=0
# for num in [1,2,3,4,5,6,7,8,9,10]:
#    sum=sum+num
# print(sum)

# print(list(range(5)))

# sums=0
# n=99
# while n>0:
#     sums=sums+n
#     n=n-2
# print(sums)

# L=['guodingkang','jinxiaonan','michael']
# for x in L:
#     print('hello!%s' %x)

# n=1
# while n<=100:
#     if(n>10):
#         break
#     print(n)
#     n=n+1
# print('end')

# n=0
# while n<10:
#     n=n+1
#     if n%2==0:
#         continue
#     print(n)
# d={'michael'}
# 'michael' in d


# s=set([1,1,2,3,4,5,2])
# s.add(6)
# print(s)
# for x in s:
#     print(x)

#6.无保存的小日记
# Diary={'12-14':'今天是星期四','12-15':'今天是星期五','12-16':'今天是星期六'}
# n=input('请输入日记代码！')
# if(not n in Diary):
#     print('创建新日记')
#     f=input('请输入日记内容:')
#     Diary[n]=f
#     print('添加%s:%s成功'%(n,Diary[n]))
# else:
#     print('查看日记%s:%s'%(n,Diary[n]))
# for x in Diary:
#     print(Diary[x])
# list=[1,2,3,4,5]
# d=set(list)
# for x in d:
#     print(x)


#7.小函数 圆的面积
# import math

# def areayuan(r):
#     try:
#          f=float(r)
#          print(f)
#          s=math.pi*f*f
#          return s
#     except ValueError:
#         return "'Please enter a valid number'"


# r1=56
# r2=56.232
# r3=78.5
# s1=areayuan(r1)
# s2=areayuan(r2)
# s3=areayuan(r3)
# print('三个圆的面积分别为%.2f,%.2f,%.2f'%(s1,s2,s3))

#8.绝对值函数
# n1='aa'
# def fun_abc(r):
#     if not isinstance(r,(int,float)): #数据类型检查isinstance()
#         raise TypeError('bad perd') #抛出异常语句
#     if(r>=0):
#         return r
#     else:
#         return -r
# print(fun_abc(n1))

#9.定义函数-求解一元二次方程
# import math
# def yiyuanerci(a,b,c):
#     for x in (a,b,c):
#         if not isinstance(x,(int,float)):
#             raise TypeError(" leixingyouwenti")
#     det=b*b-4*a*c

#     if(a==0):
#         return "x=",-c/b
#     elif det<0:
#         return wujie
#     else:
#         x1=(-b-math.sqrt(det))/(2*a)
#         x2=(-b+math.sqrt(det))/(2*a)
#         return x2,x1

# e=yiyuanerci(2, 3, 1)
# f=yiyuanerci(1, 3, -4)

# print('yiyuanerci(2, 3, 1) =', e)
# print('yiyuanerci(1, 3, -4) =', f)
# if f!=(1.0, -4.0):
#     print('测试失败')
# elif e!=(-0.5, -1.0):
#     print('测试失败')
# else:
#     print('测试成功')


#10.函数参数 -默认参数-可变参数-关键字参数 -命名关键字参数



# #默认参数
# def x2(x,n=2):
#     s=1
#     while n>0:
#         n=n-1
#         s=s*x
#     return s

# a=x2(2,n=5)
# print(a)

# def add_l(L=None):
#     if L is None:
#         L=[]
#     L.append('END')
#     return L
# print(add_l([1,2,3]))

# #可变参数
# #*numss表示把numss这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
# #参数numbers接收到的是一个tuple
# numss=[1,2,3,4]
# def cal(*numbers):
#     sum=0
#     for x in numbers:
#         sum=sum+x*x
#     return sum

# print(cal(*numss))
# print(cal(1,2,3,4))


# #关键字参数
# #这些关键字参数在函数内部自动组装为一个dict
# #函数参数测试
# def product(**y):
#     if(len(y)==0):
#         print('输入为空，请重新输入')

#     else:
#         s=1
#         for x in y:
#             if not isinstance(x,(int,float)):
#                 print('类型有误，请重新输入')
#             else:
#                 s=s*x

#     return s

# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')
#
#
#11.递归函数
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(100))


####著名的汉诺塔问题
# s=0
# def move(n,a='A',b='B',c='C'):
#     global s
#     if n==1:
#         print('%s-->%s' %(a,c))   #不管如何都是从a-->c
#         s=s+1
#         return
#     else:
#         move(n-1,a='A',b='C',c='B')    #此时把n-1个盘移到暂存区 即A——>B 此时暂存区为C
#         move(1,a='A',b='B',c='C')    #把一个盘从A——>C
#         move(n-1,a='B',b='A',c='C')       #最后把n-1个盘移到C 即B->C


# n=float(input('请输入盘子数目:'))
# print(move(n))
# print('一共移动了%.1d次'% s)
#
#12.高级特性
# L=[];
# n=1;
# while n<=99:
#     L.append(n)
#     n=n+2
# print(L)
#
#-1递归切片取值  去除头尾空格
# def trim(s):
#     if (s==""):
#         return s
#     elif(s[0]==" "):
#         return trim(s[1:])
#     elif(s[-1]==" "):
#         return trim(s[:-1])
#     else:
#         return s

# print(trim("   guodingkang   "))
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

# def trims(s):
#     if(s==""):
#         return s
#     elif(s[-1]==" "):
#         return trims(s[:-1])
#     elif(s[0]==" "):
#         return trims(s[1:])
#     else:
#         return s

# print(trims("            hhhh   "))
#
#
#-2迭代法取list中最大最小值

# def finmaxandmin(L):
#     from collections import Iterable
#     if not isinstance(L,Iterable):
#         return print('不能迭代')
#     else:
#         if len(L)==0:
#              return (None,None)
#         else:
#             min=max=L[0]
#             for x in L:
#                 if(x>max):
#                     max=x
#                 if(x<min):
#                     min=x
#             return (min,max)

# # print(finmaxandmin(12321))
# # print(finmaxandmin([]))
# print(finmaxandmin([8,7,9,5,1]))

#-3列表生成式
# L1=['213213','12312D','kKldasdK']
# L2 = [i.lower() for i in L1 if isinstance(i, str) == True]
# L3=[x*x for x in range(1,5) if(x%2)==0]

# print(L3)
# -4输出杨辉三角
# def triangles():
#   # L 输出list P 上一次结果list
#   L = P = [1]
#   while True:
#     yield L
#     P = L
#     L = []
#     for i in range(len(P) + 1):
#       if i == 0 or i == len(P):
#         L.append(1)
#       else:
#         L.append(P[i-1] + P[i])
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n=n+1
#     if(n==10):
#         break
# ads=["",2,""]
# print(ads)
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')
#-4杨辉三角   输入行数
# L 输出list P 上一次结果list
# def facc(n):
#     i=1
#     L=P=[1]
#     while i<n+1:
#         yield L
#         i=i+1
#         P=L
#         L=[]
#         for j in range(len(P)+1):
#             if(j==0 or j==len(P)):
#                 L.append(1)
#             else:
#                 L.append(P[j-1]+P[j])

# for x in facc(10):
#     print(x)
#将杨辉三角的每一行看成一个list,写一个生成器（generator）,不断输出下一行list
# def triangel(n):
#L=[1]                                                                 #定义一个list[1]
#     while True:
#         yield L                                                           #打印出该list
#         L=[L[x]+L[x+1] for x in range(len(L)-1)]        #计算下一行中间的值（除去两边的1）
#         L.insert(0,1)                                                 #在开头插入1
#         L.append(1)                                                 #在结尾添加1
#         if len(L)>10:
#             break
#                                                          #仅输出10行
# for x in triangel(10):
#     print(x)
#
#
#
# from functools import reduce
# s='23423.4234'
# n=0
# for i,x in enumerate(s):
#     if x=='.':
#         n=i
# print(n)
# DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,
#     '5':5,'6':6,'7':7,'8':8,'9':9}

# def char2float(s):
#     return DIGITS[s]
# def char2float1(s):
#     print(s*s)
#     return s*s

# s1=map(char2float,s[::-1][0:len(s)-n-1])
# print(list(s1))
# s2=map(char2float1,s1)
# print(list(s2))
#
# -6打印斐波那契数列
# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         print(b)
#         a,b=b,a+b
#         n=n+1
#     return 'done'

# print(fib(6))
#
#
# -6.1使用generator生成器打印斐波那契
# def fibg(max):
#     n,a,b=0,0,1
#     while  n<max:
#         yield b   #yield 关键字返回  下次执行从上次yield开始
#         a,b=b,a+b
#         n=n+1
#     return 'done'

# generator=fibg(6)
# for x in generator:
#     print(x)
#
# -6.2 杨辉三角使用generator打印练习 2018-1-16
#
# def yanghui(n):
#     i=0
#     P=L=[1]
#     while i<n:
#         yield L
#         i=i+1
#         P=L
#         L=[]
#         for x in range(len(P)+1):
#             if(x==0 or x==len(P)):
#                 L.append(1)
#             else:
#                 L.append(P[x-1]+P[x])

# for y in yanghui(6):
#     print(y)
#
#-7高阶函数-绝对值测验
# def absd(a,b,f):
#     return f(a)+f(b)
# print(absd(-5,4,sum))
#
#
#
# -7高阶函数-各种参数  -
# 可变参数 -list tuple
# 关键字参数-dict   **kw
# 命名关键字-单个的参数  有可变参数时不用加*
# 其余加*  如def add1(o,k_1,k_2=2,*,one,two):
#
# def poewr2(x,y):
#     q=x*y
#     return q

# def add1(o,k_1,k_2=2,*num,one,two,**kw):

#     print('k_1 power=',o(k_1,k_2))
#     print('hh power=',o(one,two))
#     P=[1]
#     for x in num:
#         P.append(x)
#     print(P)
#     for v,l in kw.items():
#         print("key=%s,value=%s"%(v,l))
#     return P

# f=poewr2
# dic11={"three":45,"four":'65'}
# ss=[10,20,30]
# d=add1(f,2,5,*ss,one=12,two=34,**dic11)
# print(d)

#-7-高阶函数-map/reduce
#  map(函数名，Iterable) 返回Iterator

# def f(x):
#     return x*x

# r=map(f,[1,2,3,4,5])
# print(list(r))
# a=str
# l=map(a,['1','2','3'])
# a=int
# l=map(a,['1','2','3'])
# print(list(l))

#reduce(函数名，Iterable)  把返回的数继续和下一个数进行计算
# from functools import reduce
# def add(x,y):
#     return x*y

# t=reduce(add,[1,2,3])
# print(t)
#
#
#---7 把str值转换为int
# from functools import reduce
# def ff(x,y):
#     return x*10+y

# def gg(a):
#     dsa={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     return dsa[a]
# e=reduce(ff,map(gg,'7345438'))
# print(e)

#整理版--lambda简化版
# from functools import reduce
# dsas={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# def strtoint(s):
#     def intvalue(a):
#         return dsas[a]
#     return reduce(lambda x,y:x*10+y,map(intvalue,s))

# b='756353534.455'
# print(strtoint(b))
#
#
#
#作业-7.3str转化为float
# from functools import reduce
# dsas={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# def strtofloat(s):
#     for j in range(len(s)):
#         if(s[j]=='.'):
#             i=j
#     m=reduce(lambda x,y:x*10+y,map(lambda s:dsas[s],s[:i]))
#     n=0
#     point=1
#     while n<len(s[i+1:]):
#         n=n+1
#         point=point*10
#     l=reduce(lambda x,y:x*10+y,map(lambda s:dsas[s],s[i+1:]))/point
#     return m+l
# print(strtofloat('1232.456'))


#网友方法7-3str转化为float
# from functools import reduce
# def str2float(s):
#     return reduce(lambda x,y:x+y/(10**len(str(y))),list(map(lambda s:reduce(lambda x,y:int(x)*10+int(y),s),s.split('.'))))
# print(str2float('1232.456'))
#1.把‘123.456‘转化为list【123，456】  map(lambda s:reduce(lambda x,y:int(x)*10+int(y),s),s.split('.'))
#其中使用s.split('.')分为’123‘和’456‘  分别运用方程int(x)*10+int(y)  得到list【123，,456】
#2.把【123，456】通过方程转化为123.456  lambda x,y:x+y/(10**len(str(y)))



#作业7.4 把不规则的字符转化成首字母大写 其他小写的形式
#

# s=['HJASDhhdjajhaj','kkDASDLALDKA','OOjJJjkLo']

# def normalis(name):
#     return name[:1].upper()+name[1:].lower()
# a=normalis
# print(list(map(a,s)))


# l=[]
# for x in range(len(s)):
#     l.append(normalis(s[x]))
# print(l)


# print(list(map(lambda name:name[:1].upper()+name[1:].lower(),s)))

#作业7.5 可以接受一个list并利用reduce()求积

# from functools import reduce
# def pord(s):
#     return reduce(lambda x,y:x*y,s)
# s=[2,3,4,5]
# print(pord(s))
# print(reduce(lambda x,y:x*y,s))




#7.6 filter 筛选函数  返回Iterator
  #得到一个list的回数(即从左向右读和从右向左读都是一样的数)
# def is_palindrome(n):

#     return n==int(str(n)[::-1])

# print(list(filter(is_palindrome,[11,232321,3,4])))


# n=123
# print(int(str(n)[::-1]))
#倒序  [::-1]
# a=['1',2,3,4,5,6]
# aa=a[::-1]
# print(aa)

#7.7 通过sorted函数对tuple  按名字或者分数 排序
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# def by_name(t):
#     return t[0]

# def by_sort(t):
#     return -t[1]
# print(sorted(L,key=by_name))
# print(sorted(L,key=by_sort))
#
#7.8 返回函数
#
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs

# f1, f2, f3 = count()
# print(f1())


# def count():
#     (lambda j:j*j,s),range(1,4)
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
#

# def creatCot():
#     def f():
#         n=0
#         while True:
#             n=n+1
#             yield n
#     sun=f()
#     def counts():
#         return next(sun)
#     return counts
# counterA=creatCot()
# print(counterA(), counterA(), counterA(), counterA(), counterA())
#
#7.9匿名函数
# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(lambda n:n % 2 == 1, range(1, 20)))
# print(L)

# def build(x,y):
#     return lambda:x*x+y*y
# q=build(5,8)
# print(q())

#7.9.1 装饰器
##装饰器一
# def logger(func):
#     def inner(*args, **kwargs):
#         print ("Arguments were:%s,%s"%(args, kwargs))
#         return func(*args, **kwargs) #2
#     return inner

# @logger
# def fool(x,y=1):
#     return x*y

# print(fool(1,2))



# def entryExit(f):
#     def new_f():
#         print ("Entering",f.__name__)
#         f()
#         print ("Exited",f.__name__)
#     return new_f

# @entryExit
# def func1():
#     print ("inside func1()")

# @entryExit
# def func2():
#     print ("inside func2()")

# func1()
# func2()
#
#
# 装饰器二
# import functools
# import time
# def metric(fn):
#     @functools.wraps(fn)
#     def fr(*args, **kwargs):
#         print('%s executed in %s ms' % (fn.__name__,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
#         return  fn(*args, **kwargs)
#     return fr

# @metric
# def fast(x, y):
#     time.sleep(0.5)
#     print('a=',x+y)
#     return x + y;

# @metric
# def slow(x, y, z):
#     time.sleep(10)
#     print('b=',x*y*z)
#     return x * y * z;

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f ==33:
#     print('测试成功!')
# elif s ==7986:
#     print('测试成功!')

#装饰器三
# import time,functools
# def metric(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         t = time.time()
#         print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#         f = func(*args, **kw)
#         print('%s excuted in %s ms' % (func.__name__,(time.time()-t)*1000))
#         print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#         return f
#     return wrapper

# @metric
# def fast(x, y):
#     time.sleep(5)
#     return x + y;

# @metric
# def slow(x, y, z):
#     time.sleep(5)
#     return x * y * z;

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')


#decorator本身需要传入参数  写法   输出的log为参数
#----1
# import time,functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print('begin %s' % text)
#             f = func(*args,**kw)
#             print('end %s'  % text)
#             return f
#         return wrapper
#     return decorator

# @log('exe')
# def test (a):
#     print('Alice')

# test('Alice')

#-----2
# import time,functools
# def logs(text):
#     def deco(fun):
#         @functools.wraps(fun)  #，需要把原始函数的__name__等属性复制到wrapper()函数中
#         def wrpr(*args,**kw):

#             print('%s begin %s in %s'%(fun.__name__,text,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
#             g=fun(*args,**kw)
#             print('%s end %s in %s'%(fun.__name__,text,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
#             return g
#         return wrpr
#     return deco

# @logs('vehicle')
# def tee(a):
#     print(a)

# @logs('vehicle')
# def tees(a):
#     time.sleep(5)
#     print(a)

# tee('guodingkang')
# tees('guodingkangs')
#
#
# 8.0偏函数  把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
#
# import functools
# int2=functools.partial(int,base=10)
# print(int2('100'))
# print(int('1112',base=10))


# 9.0 模块（Module）
#
# 假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany，按照如下目录存放：
# mycompany就是一个包 __init__.py的模块名就是 mycompany
# mycompany
#  ├─ web
#  │  ├─ __init__.py
#  │  ├─ utils.py
#  │  └─ www.py
#  ├─ __init__.py
#  ├─ abc.py
#  └─ xyz.py

# 模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。
#
# 创建自己的模块时，要注意：

#     模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
#     模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。


#9.1 使用模块

# ' a test module '
# __author__='GUO'
# import sys

# def test():
#     args=sys.argv
#     if len(args)==1:
#         print('hello  world')
#     elif len(args==2):
#         print('hello,%s!'%args[1])
#     else:
#         print('too many argument')


# if __name__=='__main__': #s是否主程序入口  别人调用时为false
#     test()


# 学过C语言的都知道，C语言定义主程序入口不就是main()函数吗，main代表了程序主入口，即和系统的接口（说白了就是命令行直接调用）。if name == 'main': 这句话的核心无非就是在判断该程序文件是否作为主程序入口罢了。 如果在命令行直接调用该程序文件，该文件作为主程序入口，name == 'main'理所当然啊。 如果在命令行调用其他程序文件，主程序入口name == 'main'自然不成立，因为main等于那个你在命令行输入的程序名。 这个东西的好处就是，别人调用时（你并非是主程序入口）后面的东西不运行，自己命令行执行时（你是主程序入口）后面的东西运行。故可以作为测试用。
#
#
#
# 10.面向对象编程   继承 封装 多态三大特性
#在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。
# class Student(object):
#     """docstring for Student"""
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score

#     def print_score(self):
#         print('%s%s'%(self.name,self.score))


# a=Student('sdsd',23)
# a.print_score()


#
# 10.1实现多进程（multiprocessing）
#multiprocessing模块就是跨平台版本的多进程模块。
#multiprocessing模块提供了一个Process类来代表一个进程对象
# from multiprocessing import Process
# import os

# def run_proc(name):
#     print('run child process %s(%s)'%(name,os.getpid()))


# if(__name__)=='__main__':
#     print('parent process %s'%os.getpid())
#     p=Process(target=run_proc,args=('guodingkang',))
#     print('child process will start')
#     p.start()
#     p.join()
#     print('child process end')

# 创建一个Process实例，用start()方法启动，
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
#
#
# 10.2  Pool 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
#
#
# from multiprocessing import Pool
# import os,time,random

# def long_timetake(name):
#     print('run now in  %s  that %s'%(name,os.getpid()))
#     start=time.time()
#     time.sleep(random.random() * 3)
#     end=time.time()
#     print('take %s runs %0.2fseconds'%(name,(end-start)))

# if __name__=='__main__':
#     print('parent process id %s',os.getpid())
#     p=Pool(10)
#     for i in range(10):
#         p.apply_async(long_timetake,args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('all subprocess done')
#
#  -10.3 子进程
#   subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
#
# import subprocess
# print('$ nslookup www.python.org')
# r=subprocess.call(['nslookup', 'http://qy.xin.com'])

# print('exit code:',r)

#-10.4 进程间的通信
#
# from multiprocessing import Process,Queue
# import os,time,random

# def write(q):
#     print('process to write %s'%os.getpid())
#     for value in ['A','B','C']:
#         print('put %s to queue'%value)
#         q.put(value)
#         time.sleep(random.random())   #写完一个睡眠一次  以便读入

# def read(q):
#     print('process to read:%s'%os.getpid())
#     while True:
#         value=q.get(True)
#         print('get %s from queue'%value)


# if __name__=='__main__':
#     q=Queue()
#     pw=Process(target=write,args=(q,))
#     pr=Process(target=read,args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()

# #
#
#
# from multiprocessing import Process, Queue
# import os, time, random

# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())

# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)

# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()





#-10.4 多线程    一个进程至少有一个线程
#
#，Python的threading模块有个current_thread()函数，
#它永远返回当前线程的实例。
#主线程实例的名字叫MainThread，子线程的名字在创建时指定，
#我们用LoopThread命名子线程
#
# import time,threading

# #新线程执行的代码:
# def loops():
#     print('thrad %s is run' %threading.current_thread().name)
#     n=0
#     while n<5:
#         n=n+1
#         print('thread %s is start >>%s'%(threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s is end'%threading.current_thread().name)



# print('thrad %s is run' %threading.current_thread().name)
# t=threading.Thread(target=loops,name='loopsname')
# t.start()
# t.join()
# print('thread %s is end'%threading.current_thread().name)



#-10.4 .1  LOCK 线程锁
#
# import time,threading

# balance=0
# lock=threading.Lock()

# def change_it(n):
#     global balance
#     balance=balance+n
#     balance=balance-n

# def run_reading(n):

#     for i in range(100000):
#         lock.acquire()
#         #获取锁
#         try:
#             change_it(n)
#         finally:
#             lock.release()
#             #释放锁

# t1=threading.Thread(target=run_reading,args=(5,))
# t2=threading.Thread(target=run_reading,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

#
##-10.4 .2 多核CPU
#
#因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
# import threading, multiprocessing

# def loop():
#     x = 0
#     while True:
#         x = x ^ 1

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()
#
#多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。

# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
# #
#
#
#10.5 类和实例
#
# class Students(object):
#     """docstring for Students"""
#     def __init__(self, name,score):
#         self.name = name
#         self.score=score

#     def getabc(self):
#         if self.score>=90:
#             return 'A'
#         elif self.score>=60:
#             return 'B'
#         else:
#             return 'C'


# xiaoming=Students('ming',95)
# print('%s>>%s' %(xiaoming.name,xiaoming.getabc()))
#
#
# 10.6访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，

# class names(object):
#     """docstring for names"""
#     def __init__(self, name,score):
#         self.__name=name
#         self.__score=score

#     def geti(self):
#         if self.__score>=90:
#             return 'A'
#         elif self.__score>=60:
#             return 'B'
#         else:
#             return 'C'
#     def getname(self):
#         return self.__name
#     def getscore(self):
#         return self.__score

# xx=names('guodingkang',99)
# print(xx.geti())
# print(xx.getname())
# print(xx.getscore())
# print('%s is %s>>%s'%(xx.getname(),xx.getscore(),xx.geti()))
# print(xx._names__name)
#
#
#
# 练习
# class Student(object):
#     """docstring for ClassName"""
#     def __init__(self, name,gender):
#         self.name = name
#         self.__gender = gender

#     def get_gender(self):
#         return self.__gender
#     def set_gender(self,gender):
#         self.__gender=gender


# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')
#
#
#
#  -10.7继承与多态
#
# class Animal(object):
#     def run(self):
#         print('animal is runing')
# def run_twice(Animal):
#     Animal.run()
#     Animal.run()

# class dog(Animal):
#     def run(self):
#         print('dog is runing')

# class cat(Animal):
#     def run(self):
#         print('cat is runing')


# run_twice(cat())
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
#
# class Tea(object):
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

#     def greet(self):
#         print('Tea is great.')

#     def print_price(self):
#         print('%s %s' % (self.name,self.price))

# class Car(object):

#     def greet(self):
#         print('Cars are great')

# class BlackTea(Tea):
#     def greet(self):
#         print('BlackTea is great.')


# class WhiteTea(Tea):
#     def greet(self):
#         print('WhiteTea is greet.')

# class Ferrari(Car):
#     def greet(self):
#         print('Ferrari is great')

# def hello(sth):
#     sth.greet()

# hello(BlackTea('Jin Junmei',10000))
# hello(WhiteTea('Gao Shan',12000))
# hello(Ferrari())
#
#
# -10.8获取对象信息
#   - a:使用type()
#
#
# import types
# def fn():
#     pass
# if type(fn)==types.FunctionType:
#     print('成功')
# if type((x for x in range(5)))==types.GeneratorType:
#     print('chengg ')
#
##
##
#-b使用isinstance()
#
# class animal(object):
#     """docstring for animal"""
#     def __init__(self, name):
#         self.name=name

# class dog(animal):
#     def __init__(self, name):
#         self.name=name

# class cat(dog):
#     def __init__(self, name):
#         self.name=name

# class dogs(cat):
#     def __init__(self, name):
#         self.name=name

# a=animal('guodingkang')
# b=dog('guodingkang')
# c=cat('guodingkang')
# d=dogs('guodingkang')
# if(isinstance(d,(animal,dog))):
#     print('success')


#-c使用dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
#
#
# setattr(obj, 'y', 19) # 设置一个属性'y'
# hasattr(obj, 'y') # 有属性'y'吗？
# getattr(obj, 'y') # 获取属性'y'

# class MyObject(object):
#     def __init__(self):
#         self.x = 9
#     def add(self):
#         return self.x + self.x

#     def pow(self):
#         return self.x * self.x

#     def sub(self):
#         return self.x - self.x

#     def div(self):
#         return self.x / self.x



# computer=MyObject()
# def run(x):
#     inp = input('method>')
#     # 判断是否有这个属性
#     if hasattr(computer,inp):
#     # 有就获取然后赋值给新的变量
#         func = getattr(computer,inp)
#         print(func())
#     else:
#     # 没有我们来set一个
#         setattr(computer,inp,lambda x:x+1)
#         func = getattr(computer,inp)
#         print(func(x))

# if __name__ == '__main__':
#     run(10)

# print(dir(computer))


#10.9实例属性和类属性

#通过self变量
# class student(object):
#     """docstring for student"""
#     def __init__(self, name):

#         self.name = name
#直接在class中定义属性，这种属性是类属性，归Student类所有
#
# class student(object):
#     name='guodingkang'

# a=student()
# a.name='hang' #实例的优先级比类属性高
# del a.name  #删除实例的name属性
# print(a.name)
# print(student.name)
#
##练习 统计人数
# class student(object):
#     count=0
#     def __init__(self, name):
#         self.name = name
#         student.count= student.count+1


# if student.count!=0:
#     print('false')
# else:
#     bart=student('guodingkang')
#     if student.count!=1:
#         print('false')
#     else:
#         hh=student('jianhii')
#         if student.count==2:
#             print('success')



#11面向对象高级编程  --多重继承、定制类、元类
#
#11.1--使用__slots__   限制实例的属性
#
#
# class student(object):
#     __slots__=('name','age')

# a=student()
# a.name='guodingkang'

# print(a.name)


# class students(student):
#    __slots__=('score')

# b=students()
# b.score=('sd')
# print(b.score)
#
#
# 11.2 使用@property
#
# class student(object):
#     def __init__(self, score,name):
#         self.__score=score
#         self.__name=name
#     def get_score(self):
#         return self.__score
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('core must be an integer!')
#         if value<0 or value>100:
#             raise ValueError('score must between 0 ~ 100!')
#         self.__score=value

# a=student(50,'45')

# print(a.get_score())


#Python内置的@property装饰器就是负责把一个方法变成属性调用的：
#只定义getter方法，不定义setter方法就是一个只读属性：
# class student(object):
#     def __init__(self):
#         self.__writh=80
#         self.__height=60
#     @property
#     def writh(self):
#         return self.__writh

#     @writh.setter
#     def writh(self,value):
#         if not isinstance(value,int):
#             raise('not int')
#         if value<1 or value>100:
#             raise('not 1~100')
#         self.__writh=value

#     @property
#     def height(self):
#         return self.__height

#     @height.setter
#     def height(self,value):
#         if not isinstance(value,int):
#             raise('not int')
#         if value<1 or value>800:
#             raise('not 1~800')
#         self.__height=value

#     @property
#     def resolution(self):
#         return (self.__writh*self.__height)


# a=student()
# print(a.writh)
# print(a.height)
# a.writh=100
# a.height=200

# print(a.resolution)
#--11.2--多重继承
#
# class animal(object):
#     def animals():
#         print('iam animal')

# class manmal(animal):
#     def manmals():
#         print('iam manmal')

# class Bird(animal):
#     def Birds():
#         print('iam Bird')

# class Flyable(object):
#     def fly(self):
#         print('Flying...')
# class Runnable(object):
#     def run(self):
#         print('Running...')


# class dog(manmal,Runnable):#可以跑还是哺乳类
#      def dogs():
#         print('iam dog')

# a=dog()

# print(a.run())
# print(a.manmals())

##-----MixIn    MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

#---多个继承
#按照继承的顺序来决定的，有同名的方法时，继承前面的类的方法





##---11.3 定制类
#
#--—__str__
#---__iter__ 一个类想被用于for ... in循环  必须实现一个__iter__()方法，
#

# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1

#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>100000:
#             raise StopIteration()
#         return self.a

# for n in Fib():
#     print(n)


#
##--__getitem__  表现得像list那样按照下标取出元素，需要实现__getitem__()方法
#
#
# class fib(object):
#     def __getitem__(self,n):
#         a,b=1,1
#         for x in range(n):
#             a,b=b,a+b
#         return a
# f=fib()
# print(f[2])


# class fib(object):
#     def __getitem__(self,n):
#         if isinstance(n,int):
#             a,b=1,1
#             for x in range(n):
#                 a,b=b,a+b
#             return a
#         if isinstance(n,slice):
#             start=n.start
#             stop=n.stop
#             if start is None:
#                 start=0
#             a,b=1,1
#             L=[]
#             for x in range(stop):
#                 if x>=start:
#                     L.append(a)
#                 a,b=b,a+b
#             return L
# f=fib()
# print(f[2:7])


#---11.4使用枚举类
# from enum import Enum
# Month=Enum('month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name,member in Month.__members__.items():
#     print(name,'=>',member,',',member.value)


# ##从Enum派生出自定义类：
# from enum import Enum,unique

# @unique
# class weekday(Enum):
#     Sun = 0 # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6


# for i in range(7):
#     print(weekday(i),i)

# for name,member in weekday.__members__.items():
#     print(name,'=>',member,',',member.value)



#---11.5元类
#
##---type()
# class Hello(object):
#     def hello(self,name='world'):
#         print('guodingkang%s'%name)


# h=Hello()
# print(h.hello())


#---而创建class的方法就是使用type()函数。
#要创建一个class对象，type()函数依次传入3个参数：
    # class的名称；
    # 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    # class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
    #
    #
# def fn(self,name='world'):
#     print('hello,%s'%name)

# guoding=type('guodin',(object,),dict
#     (hello=fn))
# g=guoding()
# print(g.hello())
#
#
#
# ---metaclass--元类
#
#----动态修改类
# class ListMetaclass(type):
#     def __new__(cls,name,bases,attrs):
#         attrs['add']=lambda self,value:self.append(value)
#         return type.__new__(cls,name,bases,attrs)



# class Mylist(list,metaclass=ListMetaclass):
#     pass

# l=Mylist()
# l.add(1)
# print(l)

#__new__()方法接收到的参数依次是：

    # 当前准备创建的类的对象；

    # 类的名字；

    # 类继承的父类集合；

    # 类的方法集合
    #
    #
    #--ORM
#总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。

# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，
#
#
#
#
#---想定义一个User类来操作对应的数据库表User，


# class Field(object):
#     def __init__(self,name,column_type):
#         self.name=name
#         self.column_type=column_type

#     def __str__(self):
#         return '<%s:%s>'%(self.__class__.__name__,self.name)


# class IntergerField(Field):
#     def __init__(self,name):
#         super(IntergerField,self).__init__(name,'varchar(100)')

# class StringField(Field):
#     def __init__(self,name):
#         super(StringField,self).__init__(name,'bigint')



# class ModelMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         if name=='Model':
#             return type.__new__(cls, name, bases, attrs)
#         print('Found model:%s'%name)
#         mappings=dict()
#         for k,v in attrs.items():
#             if isinstance(v,Field):
#                 print('Found mapping:%s==>%s'%(k,v))
#                 mappings[k]=v
#         for k in mappings.keys():
#             attrs.pop(k)
#         attrs['__mappings__']=mappings
#         attrs['__table__']=name
#         return type.__new__(cls, name, bases, attrs)

# class Model(dict,metaclass=ModelMetaclass):
#     def __init__(self,**kw):
#         super(Model,self).__init__(**kw)
#     def __getattr__(self,key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'model' has ni")

#     def __setattr__(self,key,value):
#         self[key]=ValueError
#     def save(self):
#         fields=[]
#         params=[]
#         args=[]
#         for k,v in self.__mappings__.items():
#             fields.append(v.name)
#             params.append('?')
#             args.append(getattr(self,k,none))
#         sql='insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
#         print('SQL: %s' % sql)
#         print('ARGS: %s' % str(args))

# class User(Model,IntergerField,StringField):
#     # 定义类的属性到列的映射：
#     Id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')


# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()
# 元类就是用来创建这些类（对象）的，元类就是类的类，
# 1.拦截类的创建；2.修改类；3.返回修改之后的类
# 除了使用type()动态创建类以外，要控制类的创建行为，就可以使用metaclass。

# type实际上就是一个元类，因此type()函数可以创建class
#
#
#
#
# ---12.0 错误，调试和测试
#
#
## ---12.1--try...except...finally...的错误处理机制
# try:
#     print('try..')
#     r=10/0
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except:',e)

# finally:
#     print('finally')
#     print('end')

#---使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
# def foo(s):
#     return 10/int(s)

# def bar(s):
#     return foo(s)*2
# def main():
#     try:
#         bar(0)
#     except Exception as e:
#         print('value:%s'%e)

#     finally:
#         print('finally')
#
#   --    调用栈
# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     bar('0')

# main()
#
# ----记录错误--程序打印完错误信息后会继续执行，并正常退出
# import logging
# def foo(s):
#     return 10/int(s)

# def bar(s):
#     return foo(s)*2
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#     else:
#         pass
#     finally:
#         pass

# main()
# print('end')
#
# --抛出错误
#
#--只有在必要的时候才定义我们自己的错误类型
# class Fooerror(ValueError):
#     pass

# def foo(s):
#     n=int(s)
#     if n==0:
#         raise Fooerror('error:%s'%s)
#     return 10/n
# foo('0')
#
#
#练习
#
# from functools import reduce

# def str2num(s):
#     if '.' in s:
#         return float(s)
#     else:
#         return int(s)

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)

# main()



#---12.2调试
#
#-------【断言-】-凡是用print()来辅助查看的地方，都可以用断言（assert）来替代


# def foo(s):
#     n=int(s)
#     assert n!=0,'n is zero'
#     return 10/n

# def main():
#     foo('0')

#表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
#
#断言失败，assert语句本身就会抛出AssertionError：
#启动Python解释器时可以用-O参数来关闭assert
#
#
#-----logging-----
#把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
# import logging
# logging.basicConfig(level=logging.INFO)
# s='0'
# n=int(s)
# logging.info('n=%d'%n)
# print(10/n)

#---logging的好处，它允许你指定记录信息的级别
#debug，info，warning，error等几个级别
#通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
#
#
#-----pdb------
#启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
#
#$ python -m pdb err.py
#输入命令 --l-- 来查看代码：
#输入命令 --n-- 可以单步执行代码：
#任何时候都可以输入命令--- p 变量名 ---来查看变量
#输入命令q结束调试，退出程序：
#
#
#这种通过pdb在命令行调试的方法理论上是万能的，我们还有另一种调试方法。
#
#---pbd.set_trace()---断点
#只需要import pdb，然后，
#在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
#可以用命令p查看变量，或者用命令c继续运行：
#
# import pdb
# s='0'
# n=int(s)
# pdb.set_trace()
# print(10/n)

#这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去
#
#
#
#----IDE------
##如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE
#如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有：

# Visual Studio Code：https://code.visualstudio.com/，需要安装Python插件。

# PyCharm：http://www.jetbrains.com/pycharm/

# 另外，Eclipse加上pydev插件也可以调试Python程序。


#虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器
#
#
#----12.3单元测试
#
#为了编写单元测试，我们需要引入Python自带的unittest模块，
#从unittest.TestCase继承。
#以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
#
#
#。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的
#最常用的断言就是assertEqual()：
#
#
#self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等

#另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：

# with self.assertRaises(KeyError):
#     value = d['empty']

# 而通过d.empty访问不存在的key时，我们期待抛出AttributeError：

# with self.assertRaises(AttributeError):
#     value = d.empty

#练习
#
# import unittest

# class Student(object):
#     def __init__(self, name,score):
#         self.name=name
#         self.score=score
#     def get_grade(self):
#         if self.score not in range(0,101):
#             raise ValueError
#         if self.score>=80:
#             return 'A'
#         if self.score>=60:
#             return 'B'

#         return 'C'



# class TestStudent(unittest.TestCase):
#     def test_80_to_100(self):
#         s1=Student('bart',80)
#         s2=Student('Lisr',100)
#         self.assertEqual(s1.get_grade(),'A')
#         self.assertEqual(s2.get_grade(),'A')


#     def test_60_to_80(self):
#         s1=Student('bart',60)
#         s2=Student('Lisa',79)
#         self.assertEqual(s1.get_grade(),'B')
#         self.assertEqual(s2.get_grade(),'B')

#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')

#     def test_invaild(self):
#         s1=Student('bart',-1)
#         s2=Student('lisa',101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()

# #最简单的单元测试运行方式
# if __name__=='__main__':
#     unittest.main()
#
#
#   ---12.4文档测试
#
# def fact(n):
#     '''
#     Calculate 1*2*...*n
#     >>>fact(1)
#     1
#     >>>fact(2)
#     2
#     >>>fact(3)
#     5
#     '''

#     if n<1:
#         raise ValueError()
#     if n==1:
#         return 1
#     return n*fact(n-1)


# ##调用方式
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()



###---13--IO编程
#
#

    # 基本概念：input， output，stream
    # 存在问题：输入和接收速度不匹配
    # 解决方法：同步、异步(回调--好了叫我，轮询---好了没...好了没)
    # 收获新知：编程语言都会把操作系统提供的低级C接口封装起来方便使用

#---------13.1 文件读写
#
# f=open('D:/python/hello.py','r',encoding='UTF-8')
# #如果文件不存在，open()函数就会抛出一个IOError的错误

# print(f.read())
# # 调用read()方法可以一次读取文件的全部内容，
# f.close()
#最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭
#
#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
# try:
#     f=open('D:/python/hello.py','r',encoding='utf-8')
#     print(f.read())
# except Exception as e:
#     raise

# finally:
#     if f:
#         f.close()


#-----with语句
#
#
#---但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
#
# with open('D:/python/hello.py','r',encoding='utf-8') as f:
#     print(f.read())



#要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
#
#
#
#-----file-like Object
#
    #像open()函数返回的这种有个read()方法的对象，
    #在Python中统称为file-like Object。
    #除了file外，还可以是内存的字节流，网络流，自定义流等等。
    #file-like Object不要求从特定类继承，只要写个read()方法就行。
    #StringIO就是在内存中创建的file-like Object，常用作临时缓冲
    #
    #

#----二进制文件
#
#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可#f = open('/Users/michael/test.jpg', 'rb')
#
#
#----字符编码
#
#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件

#f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
#
#
#遇到有些编码不规范的文件
#你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
#遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。
#最简单的方式是直接忽略
#
#f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
#
#
#
#
#-----写文件---
#
#写文件和读文件是一样的，唯一区别是调用open()函数时，
#传入标识符'w'或者'wb'表示写文本文件或写二进制文件
#
#
#以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）
#
#
#如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
#
#
#
# f=open('D:/Git/ceshi/gitskills/bran.txt','a')
# f.write('guodingkang20181.25')
# f.close()
# f=open('D:/Git/ceshi/gitskills/bran.txt','r')
# print(f.read())
# f.close()

#-------还是用with语句来得保险：
# with open('D:/Git/ceshi/gitskills/bran.txt','a') as f:
#     f.write('haodene ')
# with open('D:/Git/ceshi/gitskills/bran.txt','r') as f:
#     print(f.read())
# #------


#--练习
#
#
# with open('D:/Git/ceshi/gitskills/bran.txt','r') as f:
#     print(f.read())
#
#
#
#
#  ---#---------13.2---StringIO与BytesIO
#
#------StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
#
#很多时候，数据读写不一定是文件，也可以在内存中读写。

#----- StringIO-----顾名思义就是在内存中读写str。
#
# from io import StringIO
# f=StringIO()
# f.write('hello')
# print(f.getvalue())

#
#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
#
# from io import StringIO
# f=StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s=f.readline()
#     if s=='':
#         break
#     print(s.getvalue())
#
#
#
# #----- BytesIO-----要操作二进制数据，就需要使用BytesIO。
#
#
#
# from io import BytesIO
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())
#
#
#
#
# ----StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
#
#
#
# --------#---------13.3操作文件和目录
#
#
# import os
# print(os.name)



# import os
# print(os.environ)  #环境变量
# print(os.environ.get('PATH'))   #获取某个环境变量的值
#
#
# ---操作文件和目录
#
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，
# 这一点要注意一下。
# 查看、创建和删除目录可以这么调用：
#
# import os


#当前地址
# print(os.path.abspath('.'))
# os.path.split('D:\python\testdir')
#
# 创建文件
# os.mkdir('D:\python/testdirs1')
# os.mkdir('D:\python/testdirs2')



#把两个路径合成一个时，不要直接拼字符串，
#而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符

#
#
# print(os.path.join('/Users\michael', 'testdir'))    #合并
#
#
# print(os.path.split('D:\python\testdir\kk'))      #分割
#
#
#
#
# import os

# os.mkdir('D:\python/testdirs1')
#
#
# import os

# # 对文件重命名:
# os.rename('testdirs1/learning.py','testdirs1/learning1.py')

# # 删掉文件:
# os.remove('testdirs1/learning1.py')



##-----------比如我们要列出当前目录下的所有目录
#只需要一行代码：
# import os
# print([x for x in os.listdir('.') if os.path.isdir(x)])

# #要列出所有的.py文件，也只需一行代
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
#
#
#小结

# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中
#
#
#----练习
#
#---查询想要文件目录并打印

# import os
# import shutil

# def findFile(s,path='D:\python'):
#     for filename in os.listdir(path):
#         deeper_dir = os.path.join(path,filename)
#         if os.path.isfile(deeper_dir) and s in filename:
#         # 绝对路径
#             print(filename,os.path.dirname(os.path.abspath(deeper_dir)))
#             # 相对路径
#             print(filename,deeper_dir)

#         if os.path.isdir(deeper_dir):
#             findFile(s,deeper_dir)


# findFile('dsada.txt')



#-----练习 -查找某目录下的某文件  并输出路径
# import os,shutil

# def Chaxun(cxname,path):
#     for filedir in os.listdir(path):
#         Currentdir=os.path.join(path,filedir)
#         if os.path.isfile(Currentdir) and cxname in filedir:
#             #绝对路径  (所有的)
#             print(filedir,os.path.dirname(os.path.abspath(Currentdir)))
#             print(filedir,Currentdir)
#         if os.path.isdir(Currentdir):
#             Chaxun(cxname,Currentdir)



# Chaxun('.txt','D:\python')






# --------#---------13.4   序列化
#
#

# import pickle

# D=dict(name='guodingkangh',age=20,score=88)

# ##pickle.dumps()方法把任意对象序列化成一个bytes
# print(pickle.dumps(D))

# ##用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object  ---序列化写入文件
# #
# with open('D:/python/CREAT.txt','wb') as f:
#     pickle.dump(D,f)


# #可以先把内容读到一个bytes
# #然后用pickle.loads()方法反序列化出对象
# #
# #
# print(pickle.loads(pickle.dumps(D)))

# #也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象  ------从磁盘读到内存时
# #
# #
# with open('D:/python/CREAT.txt','rb') as t:
#     d=pickle.load(t)
#     print(d)

###-----------JSON
#
#如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
#
# #JSON类型     Python类型
# {}            dict
# []            list
# "string"    str
# 1234.56     int或float
# true/false  True/False
# null        None
#
#
#
#
#
#把Python对象变成一个JSON：
# import json
# d=dict(name='guodinglanh',age=20,score=88)
# print(json.dumps(d))

# #要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
# print(json.loads(json.dumps(d)))



#
###-----------JSON进阶
#
#
#很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
#
# import json

# class Student(object):
#     def __init__(self, name,age,score):
#         self.name = name
#         self.age = age
#         self.score = score

# a=Student('guodingkang',20,88)


##仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数
# 这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
#
#
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
#
# def studentjson(std):
#     return{
#     'name':std.name,
#     'age':std.age,
#     'score':std.score
#     }

# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])

# print(json.dumps(a,default=studentjson))



# #loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
# print(json.loads(json.dumps(a,default=studentjson),object_hook=dict2student))
#
#
#
#
#
# ----练习
#
# import json
# obj=dict(name='\u9773\u6653\u6960\u50bb\u903c',age=20)
# s=json.dumps(obj,ensure_ascii=False)
# print(s)

# #反序列
# print(json.loads(s))
# #
# # ensure_ascii=True,保证所有传入的非ASCII的字符都被转义，如果为false，则保持原样输出
#
#
# 这是因为json.dumps 序列化时对中文默认使用的ascii编码.
# 想输出真正的中文需要指定ensure_ascii=False：
#
#
#
#
#
#
#--------14.1ThreadLocal
#
#在多线程环境下，每个线程都有自己的数据。
#一个线程使用自己的局部变量比使用全局变量好，
#因为局部变量只有线程自己能看见，不会影响其他线程，
#
#而全局变量的修改必须加锁。
#
#ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事
##----传递全局变量
#
#
# import threading

# locals_school=threading.local()

# def process_student():
#     std=locals_school.student
#     print('hello,%s(in%s)'%(std,threading.current_thread().name))

# def process_thread(name):
#     locals_school.student=name
#     process_student()


# t1=threading.Thread(target=process_thread,args=('guodingkang',),name='process-a')
# t2=threading.Thread(target=process_thread,args=('guodingkang22',),name='process-b')
# t1.start()
# t2.start()
# t1.join()
# t2.join()


#-------不同线程 传递变量
#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
#ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
#
#
#
#
#
#------14.2进程vs线程
#异步IO
#
##------14.3分布式进程
#异步IO
#
#
#
#
###------15   正则表达式
#
#
#
#用\d可以匹配一个数字，
#用\w可以匹配一个字母或数字
#用*表示任意个字符（包括0个），
#用+表示至少一个字符，
#用?表示0个或1个字符，
#用{n}表示n个字符，
#用{n,m}表示n-m个字符：
#
#由于'-'是特殊字符，在正则表达式中，要用'\'转义
#
#
#-----15 .1进阶
#要做更精确地匹配，可以用[]表示范围
#[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；


# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）
#
#
#
# ^表示行的开头，^\d表示必须以数字开头。

# $表示行的结束，\d$表示必须以数字结束。

# -----15.2 re模块
#
#
# Python提供re模块，包含所有正则表达式的功能。
# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：

# s = r'ABC\-001
#
# import re
# text=input()
# if re.match(r'^\d{3}\-\d{3,8}$',text):
#     print('ok')
# else:
#     print('false')
# print(re.match(r'^\d{3}\-\d{3,8}$','010-12345'))



#----15.3切分字符串
# a='a b   c'.split('')
# print(a)
#
# #----15.4  贪婪匹配
#
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
# 加个?就可以让\d+采用非贪婪匹配：
# re.match(r'^(\d+?)(0*)$', '102300').groups()
# ('1023', '00')
#
#
#
#
#
# # #----15.4  编译
#
# re模块内部会干两件事情：

    # 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；

    # 用编译后的正则表达式去匹配字符串。


#，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了
#
#
# import re
# re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')
# if(re_telephone.match('010-12345')):
#     print('ok')
# print(re_telephone.match('010-12345').groups())
#
#
#
# 练习
#
#
# import re
# rename_email=re.compile(r'(<*)[w+](>*)([\w+])@([\w.]*)$')
# re_email=re.compile(r'\w+\.*\w+@\w+\.*\w+')

# def is_valid_email(addr):
#     if(re_email.match(addr)):
#         return True
#     else:
#         return False

# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')

# def name_valid_email(addr):
#     if(re_email.match(addr)):
#         return re_name.match(addr).group(2)
#     else:
#         return False

# print(name_valid_email('<Tom Paris>tom@voyager.org'))
# assert name_valid_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
# assert name_valid_email('tom@voyager.org') == 'tom'
# print('ok')



#-----16.------常用内建模块
#
#
#
#----16.1  str转换为datetime datetime转换为str
# from datetime import datetime
# print(datetime.now())
# cday=datetime.strptime('2015-6-5 18:19:56','%Y-%m-%d %H:%M:%S')
# print(cday)
# now=datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))
#
# ---16.2 datetime加减
# from datetime import datetime,timedelta
# now=datetime.now()
# now+=timedelta(hours=-10)
# now+=timedelta(days=2,hours=-10)
# print(now)
#
#
#
# #-----17.------常用第三方模块
#
#
# -17.1---Pillow---图像处理标准库
#
#---简单缩小保存
# from PIL import Image
# im=Image.open('muma0722-LY_-郭定康-4653---1寸.jpg')

# w,h=im.size
# print('image size；%sx%s'%(w,h))
# im.thumbnail((w/2,h/2))
# print('Resize image to: %sx%s' % (w//2, h//2))
# im.save('guodingkang.jpg','jpeg')
#


#---生成字母验证码
#
# from PIL import Image,ImageDraw,ImageFont,ImageFilter
# import random


# #随机字母：
# def rndChar():
#     return chr(random.randint(65,90))
# #随机颜色：
# def rndColor():
#     return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# #随机颜色2
# def rndColor2():
#     return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

# #确定大小和格式
# width=60*4
# height=60
# image=Image.new('RGB',(width,height),(255,255,255))

# #创建font对象  字体
# font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',36)
# #画布 创建draw对象
# draw=ImageDraw.Draw(image)
# #填充每个像素
# for x in range(width):
#     for y in range(height):
#         draw.point((x,y),fill=rndColor())

# #输出文字 字符
# for t in range(4):
#     draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
# #模糊
# image=image.filter(ImageFilter.BLUR)
# #保存
# image.save('code.jpg','jpeg')
#
#
# # -17.2---Requests---用于访问网络资源
#
# import requests
# r=requests.get('https://www.baidu.com/')
# print(r.status_code)
# print(r.text)
#
# # # -17.3---Chardet---用它来检测编码
#
#
# print(chardet.detect(b'hello,world'))
#
#
#
# # # # -17.4---psutil---获取系统信息
#
# import psutil

# #我们先来获取CPU的信息：
# print(psutil.cpu_count())
# print(psutil.cpu_count(logical=False))

# #统计CPU的用户／系统／空闲时间：
# print(psutil.cpu_times())
# #获取内存信息
# #使用psutil获取物理内存和交换内存信息，分别使用：
# print(psutil.virtual_memory())
# print(psutil.swap_memory())


# #获取磁盘信息
# #可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：

# print(psutil.disk_partitions())
# print(psutil.disk_usage('/') )
# print(psutil.disk_io_counters())

# #获取网络信息
# #psutil可以获取网络接口和网络连接信息：
# #
# print(psutil.net_io_counters())
# print(psutil.net_if_addrs())
# print(psutil.net_if_stats())

# #要获取当前网络连接信息，使用net_connections()：
# print(psutil.net_connections())

# #获取进程信息
# #通过psutil可以获取到所有进程的详细信息
# print(psutil.pids())
# p = psutil.Process(3776)
# pritn(p.name())
#
#
# #psutil还提供了一个test()函数，可以模拟出ps命令的效果
# print(psutil.test())
#
#
# 17.5---virtualenv为应用提供了隔离的Python运行环境，解决了不同应用间多版本的冲突问题。
#
#
#
#-----18.0 ----图形界面 GUI
#
# Python支持多种图形界面的第三方库，包括：

#     Tk

#     wxWidgets

#     Qt

#     GTK
#
#
#Python自带的库是支持Tk的Tkinter，使用Tkinter


# from tkinter import *
# import tkinter.messagebox as messagebox

# class Application(Frame):
#     def __init__(self,master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.creatWidgets()

#     def creatWidgets(self):
#         self.helloLabel=Label(self,text='hello world')
#         self.helloLabel.pack()
#         self.quitButton=Button(self,text='Hello',command=self.hello)
#         self.quitButton.pack()
#     def hello(self):
#         name='world'
#         messagebox.showinfo('Message','Hello,%s'%name)

# app=Application()
# app.master.title('hello,world')
# app.mainloop()



#-----19.0  -----网络编程--TCP/IP    TCP编程  UDP编程
#
#Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
#
#
#
#客户端
#
#创建一个基于TCP连接的Socket，可以这样做
#
#
# import socket

# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# #创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接
# s.connect(('www.sina.com.cn',80))

# #因为80端口是Web服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，等等。端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用
# #
# s.send(b'GET/HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnetion:colse\r\n\r\n')


# buffer=[]
# while True:
#     d=s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data=b''.join(buffer)
# s.close()

# header,html=data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# with open('sina.html','wb')as f:
#     f.write(html)
#
#
#     20 -冒泡排序
#
# def mao(n):
#     for i in range(len(n)):
#         for j in range(len(n)-i-1):
#             if n[j]>n[j+1]:
#                 n[j],n[j+1]=n[j+1],n[j]
#     return n

# n=[4,3,7,1,9]
# print( mao(n))

# def change_bubble(lt):
#     lenth=len(lt)
#     for i in range(1,lenth):
#         for j in range(0,lenth-i):
#             if lt[j]>lt[j+1]:
#                 lt[j],lt[j+1]=lt[j+1],lt[j]

#     return lt

# lt=[2,1,89,4,3,56,788,14,256,8895]

# print(change_bubble(lt))
#
#
# ---------------------------------------------------------------------------------------
#
# ---------------------------2018-9-25 面试题--------------------------------------------
#
# # 1.一行代码实现1--100之和
# suma=sum(range(0,101))
# print(suma)


# 2.   5个常用的标准库
# os 操作系统相关
# sys  用于命令行参数
# datatime  处理时间
# re  正则匹配默认是贪婪匹配，也就是匹配尽可能多的字
# math 数学计算
#
# 3.字典如何删除键和新增

# dic={'name':'gdk','age':'23'}
# dic2={'ages':'9090'}
# dic.update(dic2)
# print(dic)
#4.GIL
#GIL是python全局解释器锁，当一个进程又多个线程时，一个线程运行python程序时会霸占python解释器，其他线程无法运行。等该线程云子那完成后才能执行  如果遇到耗时操作，会自动解除并不是同时进行
#
#
#6.列表去重
#
# def list_re(lt):
#     a=set(lt)
#     print(a)


# print(list_re([1,5,6,3,1,2,5,8]))
#
# 7.可变参数*args 接受的是不定数量的参数 并组装成list列表
#  关键字参数**kwargs  接受的不定长度的键值对   组合成dict
#
#
#
#  8.简述面向对象中__new__和__init__ 的区别
#  __init__是初始化方法  创建对象后立即调用  可接受参数
#  __new__是创建实例    至少要有一个参数cls  当前实例
#
#  9新建一个文件读取文件
#

# with open('E:\Python2018\hello.py','r',encoding='utf-8') as f:
#     print(f.read())
#
# 10. 使用推导式  匿名函数

# from functools import reduce

# lt=[1,2,3,5,7,8,9,4]
# res=map(lambda x:x**2,lt)

# red=reduce(lambda x,y:x+y,lt)
# for i in res:
#     print(i)

# print(red)
#
#
# 11.随机生成整数 随机小数  0-1之间小数
#
# import random
# import numpy as np

# print(random.randint(1,10))
# print(random.random())
# print(np.random.randn(
#     ))

# 12.正则匹配
#

# import re

# str='<div class="name">呵呵</div>'
# reg=re.compile('<div class=".*?">(.*?)</div>')
# res=re.findall(reg,str)
# print(res)
#
#
# 13.断言 assert()
#断言成功，则程序继续执行，断言失败，则程序报错


# a=3
# assert(a>10)
# print('success')
#
# 14.消除重复  distinct
# 15.常见的linux指令
# 16.python2和python3的区别
# 1.print必须用括号
# 2.range()返回迭代器
# 3.使用ascii编码  3使用utf-8
# 4，raw_input()   变成input()
#
#
# 17.列出python中可变对象和不可变对象
#
# 不可变  string tuple  就是一旦声明、定义以后，就不能再变
# 可变  list


# 18、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl
# s = "ajldjlajfdljfddd"
# s=set(s)
# s=list(s)
# s.sort()
# res="".join(s)
# print(res)



# 19.join合并
# delimiter = ','
# mylist = ['Brazil', 'Russia', 'India', 'China']
# print (delimiter.join(mylist))
#
#
#
#20.用lambda函数实现两个数相乘
#
# sum=lambda a,b:a*b
# print(sum(3,4))


#21.利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
#
# rom collections import Counter

# a="kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
# res=Counter(a)
# print(res)
#

# 22.字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"
#
#
# import re
# a = "not 404 found 张三 99 深圳"
# list=a.split(" ")
# print(list)
# reco=re.compile('\d+|[a-zA-Z]+')
# res=re.findall(reco,a)
# for i in res:
#     if i in list :
#         list.remove(i)
# new_str=" ".join(list)
# print(res)
# print(new_str)
#
#
# 23.filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def fn(a):
#     return a%2==1
# newlist=[i for i in filter(fn,a)]
# newlist1=[i for i in a if i%2==1]
# print(newlist,newlist1)

#24.两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]

# def merge(list1,list2):
#     newlist=[]
#     while list1 and list2:
#         if list1[0]<list2[0]:
#             newlist.append(list1[0])
#             list1.remove(list1[0])
#         else:
#             newlist.append(list2[0])
#             list2.remove(list2[0])
#     if list1:
#         newlist.extend(list1)
#     if list2:
#         newlist.extend(list2)

#     print(newlist)


# list1=[1,5,7,9]
# list2=[1,2,2,3,6,7,8,9]
# merge(list1,list2)


#25.用python删除文件和用linux命令删除文件方法
#
#linux   rm file
#
#python
#

# import os

# os.remove('')

#26.打印当前时间
# import datetime
# index=datetime.datetime.now()
# print(index.hour)
# print(index.minute)
# print(index.year)
# print(index.second)



#27.数据库优化查询方法

  #1、选取最适用的字段属性 --字段的宽度设得尽可能小
  #2、使用连接（JOIN）来代替子查询(Sub-Queries)
  #3、使用联合(UNION)来代替手动创建的临时表
  #4、事务
  #6、使用外键
  #该参数保证当customerinfo表中的一条客户记录被删除的时候，salesinfo表中所有与该客户相关的记录也会被自动删除。
  #如果要在MySQL中使用外键，一定要记住在创建表的时候将表的类型定义为事务安全表InnoDB类型。该类型不是MySQL表的默认类型。定义的方法是在CREATETABLE语句中加上TYPE=INNODB。如例中所示。
  #7、使用索引
  #一般说来，索引应建立在那些将用于JOIN,WHERE判断和ORDERBY排序的字段上
  #8、优化的查询语句
  #
  #
  #
  #
  #
#28.请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
#highcharts
#
#
#29.写一段自定义异常代码

# import json, logging, inspect, functools

# class DatabaseException(Exception):
#     def __init__(self,err='数据库错误',message='数据库错误'):
#         super(DatabaseException, self).__init__(message)
#         self.err=err


# try:
#     s=[]
#     if not s:
#         raise DatabaseException()
# except ValueError:
#     print('ss')
#
#
#
#     30.正则表达式匹配中，（.*）和（.*?）匹配区别？

# 比如说匹配输入串A: 101000000000100
# 使用 1.*1 将会匹配到1010000000001,
# 匹配方法: 先匹配至输入串A的最后, 然后向前匹配, 直到可以匹配到1, 称之为贪婪匹配。
# 使用 1.*?1 将会匹配到101,
# 匹配方法: *匹配下一个1之前的所有字符, 称之为非贪婪匹配。

#31.简述Django中的orm
#
# ORM是“对象-关系-映射”的简称，主要任务是：

#     根据对象的类型生成表结构  元类
#     将对象、列表的操作，转换为sql语句    类方法
#     将sql查询到的结果转换为对象、列表



#  32.二维数组一维数组互换
#
#  [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
#
#1.一句话
# new=[1,2,3,4,5,6]
# list=[new[i:i+2] for i in range(0,len(new),2)]
# print(list)
#
# 2.使用zip
# a=[1,2,5,6]
# b=[3,4,8,9]
# news=[i for i in zip(a,b)]
# print(news)




# list=[[1,2],[3,4],[5,6]]

# #1.使用flatten
# # from compiler.ast import flatten
# # newlist=flatten(list)
# # print(newlist)

# #2.土方法  嵌套循环
# new=[]
# # new.extend(for i  in range (0,len(list)))
# new=[list[i][j] for  i  in range(0,len(list)) for j in [0,1]]
# print(new)
#
#
#
# 33. x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果

# x="abc"
# y="def"
# z=["d","e","f"]

# print(x.join(y))
# print(x.join(z))
#
# 34.、举例说明异常模块中try except else finally的相关意义
# try:
#     print(8/int(input("请输入一个非零整数：")))
# except ZeroDivisionError:
#     print("除数不能为0")
# except ValueError:
#     print("请重新输入")
# except Exception as reason:
#     print("未知类型错误：" % reason)
# else:
#     print("你真棒，一次就获得正确的结果")
# finally:
#     print("不管结果如何，你做了就是好孩纸")
#     print("如果你喜欢这段代码，请给我点赞哟，么么哒")


#35.替换
# a='zhangming  98'
# a=a.replace(' ','100')
# print(a)

#36.常用sql
# 1.创建新表
# create table tabname(col1 type1 [not null] [primary key],col2 type2 [not null],..)

# 2.删除表
# drop table tabname

# 3.查询：select * from table1 where 范围

# 4.插入：insert into 表名(字段名1,字段名2) values(值1,值2)

# 5.删除：delete from table1 where 范围

# 6.修改：update 表名 set 修改的字段名=修改的字段值 where 范围

# import re
# url='https://sycm.taobao.com/bda/tradinganaly/overviewget_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
# res=re.compile('.*?dateRange=(.*?)%7C.*?')
# list=re.findall(res,url)
# print(list)
#
# 37  排序
#

# def change_bobule(list):
#     lenth=len(list)
#     for  i in range(1,lenth):
#         for j in range(0,lenth-i):
#             if list[j]>list[j+1]:
#                 list[j],list[j+1]=list[j+1],list[j]
#     return list
# list=[2,3,5,4,9,6]


#38.三种打印方式
# print(change_bobule(list))
# print('常量 PI 的值近似为：%s' % math.pi)
# print('常量 PI 的值近似为： {}'.format(math.pi))


#39.列出常见的状态码和意义
#
#200    成功  204 没有主体返回
#300     请求已被转移  301  永远重定向  302 临时重定向
#400  请求报文出错  401  认证失败         403  请求被拒绝        404 资源找不到
#500  服务器内部错误   503服务器超负载或停机维护


#40 .web性能优化
#
#1，减少http请求  使用缓存  避免页面跳转  避免404
#2，css置顶   避免css表达式  js置底  去除重复的脚本  减少dom元素的访问
#3。优化图像
#
#
#41.True使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
#
# dic={"name":"zs","age":18}
# del dic['name']
# dic['name']='gdk'
# dic.pop('name')
# print(dic)
#
# 42.常见的数据库存储引擎
#
# InnoDB是事务型数据库的首选引擎，支持事务安全表（ACID），其它存储引擎都是非事务安全表，支持行锁定和外键，MySQL5.5以后默认使用InnoDB存储引擎。支持外键的存储引擎
#
#
# MyISAM拥有较高的插入、查询速度，但不支持事务，不支持外键。
#
#
# MEMORY存储引擎将表中的数据存储到内存中，为查询和引用其他表数据提供快速访问
#
#
#
# InnoDB： 支持事务处理，支持外键，支持崩溃修复能力和并发控制。如果需要对事务的完整性要求比较高（比如银行），要求实现并发控制（比如售票），那选择InnoDB有很大的优势。如果需要频繁的更新、删除操作的数据库，也可以选择InnoDB，因为支持事务的提交（commit）和回滚（rollback）。
# MyISAM： 插入数据快，空间和内存使用比较低。如果表主要是用于插入新记录和读出记录，那么选择MyISAM能实现处理高效率。如果应用的完整性、并发性要求比较低，也可以使用。
#  ·
# MEMORY： 所有的数据都在内存中，数据的处理速度快，但是安全性不高。如果需要很快的读写速度，对数据的安全性要求较低，可以选择MEMOEY。它对表的大小有要求，不能建立太大的表。所以，这类数据库只使用在相对较小的数据库表。
#
#
#
#
# 44，简述同源策略
#
# 同源策略（Same origin policy）是一种约定，它是浏览器最核心也最基本的安全功能，如果缺少了同源策略，则浏览器的正常功能可能都会受到影响。可以说Web是构建在同源策略基础之上的，浏览器只是针对同源策略的一种实现。



#45. 说说Cookie和Session的区别？
#   
#    1、Cookie和Session都是会话技术，Cookie是运行在客户端，Session是运行在服务器端。
#   
#    2、Cookie有大小限制以及浏览器在存cookie的个数也有限制，Session是没有大小限制和服务器的内存大小有关。

#    3、Cookie有安全隐患，通过拦截或本地文件找得到你的cookie后可以进行攻击。

#    4、Session是保存在服务器端上会存在一段时间才会消失，如果session过多会增加服务器的压力。


#46.简述多进程和多线程
#
#程是操作系统进行资源分配的单位   一个进程可以包含多个线程
#
#多线程是为了使得多个线程并行的工作以完成多项任务，以提高系统的效率。线程是在同一时间需要完成多项任务的时候被实现的
#
#
#47。any()和all()用法   判断是否空对象  是空返回False
#
#
#any(x)判断x对象是否为空对象，如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true
#
#all(x)如果all(x)参数x对象的所有元素不为0、''、False或者x为空对象，则返回True，否则返回False
#
#all()有一个为空就返回False
#
#
#
#48.copy.deepcopy区别
#
#浅拷贝copy拷贝一个对象，但是对象的属性还是引用原来的，
#deepcopy拷贝一个对象，把对象里面的属性也做了拷贝，deepcopy之后完全是另一个对象了。改变与否不受其他对象的影响。
#

#49.生成器
# def gen():
#     for i in range(3):
#         yield i
# print(gen())
# for i in gen():

#     print(i)
#
#
# 50.a = "  hehheh  ",去除收尾空格
# a = "  hehheh  "
# print(len(a))
# a=a.strip()
# print(len(a))
#
#

#   101-200素数
# def Is_shusu():
#     num=0
#     for i in range(101,201):
#         iss=0
#         for j in range(2,i):
#             if i%j==0:
#                 iss+=1
#         if iss==0:
#             print(i)
#             num+=1
#     print('素数有%d'%num)

# Is_shusu()


#---抽象工厂模式

# class Shoe:
#     """抽象产品类  基类  鞋"""
#     def corss(self):
#         pass


# class LeatherShoe(Shoe):
#     """皮鞋  具体产品"""
#     def corss(self):
#         print('穿皮鞋 走啦！！')

# class SoccerShoe(Shoe):
#     """球鞋  具体产品"""
#     def corss(self):
#         print('穿球鞋 走啦！！')



# class ShoeFactory:
#     """抽象工厂 类"""
#     def make_shoe(self):
#         pass


# class LeatherShoeFactory(ShoeFactory):
#     """皮鞋工厂"""
#     def make_shoe(self):
#         return LeatherShoe()


# class SoccerShoeFactory(ShoeFactory):
#     """球鞋工厂"""
#     def make_shoe(self):
#         return SoccerShoe()



# def anli_call():
#     factory=LeatherShoeFactory()
#     for i in range(3):
#         shoe=factory.make_shoe()


# def henda_call():
#     factory=SoccerShoeFactory()
#     for i in range(3):
#         shoe=factory.make_shoe()



# anli_call()
# henda_call()
#
#
#
#


# #   题目描述  斐波那契数列-开始
# # 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。

# # n<=39

# #------测试斐波那契数列两种方法【执行时间】  测试

# '''
# 装饰器-执行时间
# '''
# import time
# def timer(func):

#     def decor(*args):
#         start_time=time.time()
#         res=func(*args)
#         end_time=time.time()
#         print('running time is :{}'.format(end_time-start_time))
#         return res
#     return decor


# #简单的动态规划，
# #以一定的空间代价避免代价更大的重复计算的栈空间浪费
# @timer
# def Fibonacci(n):
#     # write code here
#     f0,f1=0,1
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     else:
#         a=0
#         for i in range(2,n+1):
#             a=f0+f1
#             f0=f1
#             f1=a
#         return a
# #递归方法   耗资源  重复计算
# def Fibonaccis(n):

#     if n==0:
#         return  0
#     if n==1:
#         return 1
#     else:
#         f=Fibonaccis(n-1)+Fibonaccis(n-2)
#         return f
# @timer
# def functions(n):
#     return Fibonaccis(n)


# if __name__ == '__main__':
#     n=40
#     start=time.time()
#     print(Fibonacci(n))
#     end=time.time()
#     print('one--  running time is {}'.format(end-start))

#     starts=time.time()
#     print(functions(n))
#     ends=time.time()
#     print('two--  running time is {}'.format(ends-starts))

# #   题目描述  斐波那契数列-结束
#
#
#
######-----剑指offer-----第8题----
#
#题目描述 ------跳台阶问题---开始--------
#
#一只青蛙一次可以跳上1级台阶，也可以跳上2级。
#求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。


#--解法一--递归法---
# def jumpFloor(number):
#     # write code here
#     stuple={1:1,2:2}
#     if isinstance(number,int) and number >0:
#         if number in stuple.keys():
#             return stuple[number]
#         else:
#             return jumpFloor(number-1)+jumpFloor(number-2)
#     else:
#         print('zhe number is error')



#解法2-----递推法------
#
#
# def jumpFloors(number):
#     stuple={1:1,2:2}
#     n=3
#     h1,h2=1,2
#     temp=0
#     if isinstance(number,int) and number > 0:
#         if number in stuple.keys():
#             return stuple[number]
#         else:
#             while n<=number:
#                 temp=h1
#                 h1=h2
#                 h2=temp+h1
#                 n+=1
#             return h2
#     else:
#         print('zhe number is error')

# if __name__=='__main__':
#     print(jumpFloor(5))
#     print(jumpFloors(5))


#问题描述----开始
##----Python初学者练习：有n个人围成一个圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位

#  n=int(input('请输入人数：'))
# li_c=list(range(0,n))
# count=0
# while len(li_c)>2:
#     li_co=li_c[:]
#     for i in range(0,len(li_co)):
#         count+=1
#         if count%3==0:
#             li_c.remove(li_co[i])
# print('最后留下的是原来的第{}号'.format(li_c))

#问题描述----结束
#
#
######-----剑指offer-----第10题----
#
#题目描述 ------矩形覆盖问题---开始--------
#我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
#
#---解法一-----递归法
# def RectCover(n):
#     if n<=1:
#         return 1
#     elif n==2:
#         return 2
#     else:
#         return RectCover(n-1)+RectCover(n-2)

#---解法2-----递推法
#
# def RectCovers(n):
#     if n<1:
#         return 0
#     p=q=r=0
#     for i in range(1,n+1):
#         if i==1:
#             p=q=r=1
#         elif i==2:
#             p=r=2
#         else:
#             r=q+p
#             p=q
#             q=r
#     return r

# print(RectCovers(3))
