# -*-coding:utf-8-*-
# import math
# import string

# for letter in 'Python':
#     if letter == 'h':
#         break
#     print 'Current letter:',letter

# var = 10
# while var > 0:
#     print 'current variable value:',var
#     var = var-1
#     if var ==5:
#         break

# print math.modf(12.56)
# print math.sqrt(4)

# import random

# print "choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9])
# print "choice('A String') : ", random.choice('A String')
# print math.pi

# var1 = 'Hello\a World!'
# var2 = """heh \t ss
# jjjjj \t dfsf

# """
# var3 = 'jjjjj \other dfsf'
# hi = '''hi 
# there'''
# he = 'jh'
# print "更新字符串 :- ", var1[4:6] + 'Runoob!'
# print var1
# print var2
# print var3
# print hi
# print "My name is %s and weight is %d kg!"%('zara',21)
# print string.capitalize('java.md')
# print he.center(5)

# d2={'span':2,'han':'sd','ss':4}
# print d2
# print d2.keys()
# # d2.clear()
# # del d2
# for value in d2:
#     print value
# print d2.copy()

# dict = {'Name': 'Zara', 'Age': 27}

# print "Value : %s" %  dict.get('Age')
# print "Value : %s" %  dict.get('Sex', 'None')
# print "Value : %s" %  dict.setdefault('Sex', None)
# print dict
# print dict.items()

# import time

# ticks = time.time()
# print ticks

# localtime = time.localtime()
# print localtime 

# localtime = time.asctime(time.localtime())
# print localtime

# print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

# print time.strftime("%X %Z %j %U %W %c %A %B %d %H:%M:%S %Y", time.localtime()) 

# a = "Sat Mar 28 22:24:24 2016"
# print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))


# import calendar

# cla = calendar.month(2016,12)
# print cla

# def printme(str):
#     print str
#     return

# printme('wo kankan')

# # 可写函数说明
# def printinfo( arg1, *vartuple ):
#    "打印任何传入的参数"
#    print "输出: "
#    print arg1
#    for var in vartuple:
#       print var
#    return;

# 调用printinfo 函数
# printinfo( 10 );
# printinfo( 70, 60, 50 );

# from mukuai import zhetiame

# c = zhetiame('s')



# 打开一个文件
# fo = open("foo.txt", "r+")
# str = fo.read(10);
# print "读取的字符串是 : ", str

# # 查找当前位置
# position = fo.tell();
# print "当前文件位置 : ", position

# # 把指针再次重新定位到文件开头
# position = fo.seek(0, 1);
# str = fo.read(10);
# print "重新读取字符串 : ", str
# # 关闭打开的文件
# fo.close()


# # 定义函数
# def mye( level ):
#     if level < 1:
#         raise Exception("Invalid level!", level)
#         # 触发异常后，后面的代码就不会再执行

# try:
#     mye(0)                
# except "Invalid level!":
#     print 1
# else:
#     print 2
#     
# class Employee:
#     '''所有员工的基类'''
#     empCount = 0
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print "Total Employee %d"% Employee.empCount
#
#     def displayEmployee(self):
#         print "Name:",self.name,"Salary:",self.salary
#
# emp1 = Employee("Zara",200)
# emp2 = Employee("Manni",1000)
#
# emp1.age = 15
#
# emp1.displayEmployee()
# emp2.displayEmployee()
# emp1.displayCount()
# print emp1.age
#
# print "Total Employee %d"% Employee.empCount
# print dir(Employee)
# print Employee.__doc__
# print getattr(emp1,'age')
# print hasattr(emp1,'age')
# print hasattr(Employee,'empCount')
#
# print setattr(Employee,'age',7)
# print Employee.age
# print hasattr(Employee,'age')
# print emp1.__dict__
# print Employee.__dict__
# print Employee.__module__
# from mukuai import zhetiame
#
# print zhetiame.__module__

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print class_name,'销毁'
#
# pt1=Point()
# pt2 = pt1
# pt3= pt1
#
# print id(pt1),id(pt2),id(pt3)
#
# del pt1
# # del pt2
# del pt3
#
#
# class Parent:
#     parentAttr =  100
#     def __init__(self):
#         print "调用父类构造函数"
#
#     def parentMethod(self):
#         print "调用父类方法"
#
#     def setAttr(self,attr):
#         Parent.parentAttr = attr
#
#     def getAttr(self):
#         print "父类属性:",Parent.parentAttr
#
# class Child(Parent):
#     def __init__(self):
#         print "调用子类构造方法"
#
#     def childMethod(self):
#         print '调用子类方法 child method'
#
# c=Child()
# c.childMethod()
# c.parentMethod()
# c.setAttr(200)
# c.getAttr()
# print c.parentAttr
#
# class Parent:        # 定义父类
#    def myMethod(self):
#       print '调用父类方法'
#
# class Child(Parent): # 定义子类
#    def myMethod(self):
#       print '调用子类方法'
#
# c = Child()          # 子类实例
# c.myMethod()         # 子类调用重写方法
#
# class Vector:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     # def __str__(self):
#     #     return 'Vector (%d,%d)'%(self.a,self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a , self.b+ other.b)
#
# v1 = Vector(2,10)
# v2 = Vector(5,-2)
#
# print v1 + v2


import re

print re.match('www','www.runoob.com').span()
print re.match('com','www.runoob.com')

line = 'Cats are smarter than dogs'

matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

# if matchObj:
#     print 'matchObj.group():',matchObj.group()
#     print "matchObj.group(1) : ", matchObj.group(1)
#     print "matchObj.group(2) : ", matchObj.group(2)
# else:
#     print "no mathc!!"
#
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

if matchObj:
   print "match --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print "search --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"


phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是: ", num

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是 : ", num