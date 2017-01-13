# -*-coding:utf-8-*-
#导入socket模块
import socket

#创建socket对象
s = socket.socket()

#获取本地主机名
host = socket.gethostname()

#设置好端口号
port = 12345

s.connect((host,port))
print s.recv(1024)
s.close()