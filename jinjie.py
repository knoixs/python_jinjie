# -*-coding:utf-8-*-
# 2-3
# import math
# def add(x,y,f):
#     return f(x)+f(y)
#
# print (add(25,9,math.sqrt))


# #2-4
# def format_name(s):
#     return s.capitalize()
#
# print map(format_name, ['adam', 'LISA', 'barT'])


# #2-6
# import math
#
# def is_sqr(x):
#     r = int(math.sqrt(x))
#     return r*r==x
#
# print filter(is_sqr, range(1, 101))


# #2-7
# def cmp_ignore_case(s1,s2):
#     if s1.lower()>s2.lower():
#         return 1
#     if s1.lower()<s2.lower():
#         return -1
#     return 0
#
# print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

# print ('Hi,{name},{message}'.format(name='Tom',message='hihao'))


# def new_counter(n):
#
#     class Counter(object):
#         def __init__(self, num):
#             self.num =num
#
#         def __call__(self):
#             self.num += 1
#             return self.num
#
#     return Counter(n)
#
# c1 = new_counter(10)
# c2 = new_counter(20)
# print c1(), c2(), c1(), c2()


# # 2-8
# def calc_prod(lst):
#     def lazy_prod(x, y):
#         return x * y
#
#     def prod():
#         return reduce(lazy_prod, lst)
#
#     return prod
#
#
# f = calc_prod([1, 2, 3, 4])
# print f()
#

# #2-1
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print f1()

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f(j):
#             def g():
#                 return j*j
#             return g
#         r=f(i)
#         fs.append(r)
#     return fs
#
# f1, f2, f3 = count()
# print f1(), f2(), f3()
#
# print(cmp(2,1))

# #2-10匿名函数
# def is_not_empty(s):
#     return s and len(s.strip()) > 0
#
# print filter(lambda x:x and len(x.strip())>0, ['test', None, '', 'str', '  ', 'END'])


# def deco(func):
#     print("before myfunc() called.")
#     func()
#     print("  after myfunc() called.")
#     return func
#
#
# def myfunc():
#     print(" myfunc() called.")
#
#
# myfunc = deco(myfunc)
#
# myfunc()
# myfunc()


# from Tkinter import *
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Hello, world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()
#
# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()


#2-12
# def log(f):
#     def fn(x):
#         print 'call'+f.__name__+'()..'
#         return f(x)
#     return fn
#
# @log
# def factorial(n):
#     return reduce(lambda x,y: x*y, range(1, n+1))
# print factorial(10)

# import time
# def performance(f):
#     def fn(*args,**kwargs):
#         t1=time.time()
#         r=f(*args,**kwargs)
#         t2=time.time()
#         print 'call %s() in %fs'%(f.__name__,(t2-t1))
#         return r
#     return fn
#
# @performance
# def factorial(n):
#     return reduce(lambda x,y:x*y,range(1,n+1))
# print factorial(10)