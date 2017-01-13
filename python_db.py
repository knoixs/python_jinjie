# -*-coding:utf-8-*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user="testuser",
                     passwd="test1234",
                     db="TESTDB", )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

#
# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone方法获取一条数据库。
# data = cursor.fetchone()
#
# print "Database version:%s" % data
#
# # 关闭数据库连接
# db.close()


# 新建数据库
# # 打开数据库连接
# db = MySQLdb.connect(host="localhost",
#                      port=3306,
#                      user="testuser",
#                      passwd="test1234",
#                      db="TESTDB", )
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # 如果数据表已经存在，使用execute()方法删除表
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 创建数据表SQL语句
# sql = """CREATE TABLE EMPLOYEE(
# FIRST_NAME CHAR(20) NOT NULL ,
# LAST_NAME CHAR(20),
# AGE INT ,
# SEX CHAR (1),
# INCOME FLOAT ,
# zhenshi CHAR (2))
#
# """
#
# cursor.execute(sql)
#
# #关闭数据库
# db.close()


# 插入新数据

# #打开数据库连接
# db = MySQLdb.connect(host="localhost",
#                      port=3306,
#                      user="testuser",
#                      passwd="test1234",
#                      db="TESTDB",
#                      )
#
# #使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# #SQL语句
#
# sql = """
# INSERT INTO EMPLOYEE(
# FIRST_NAME,LAST_NAME,AGE,SEX,INCOME,ZHENSHI)
# VALUES(
# 'Mac','Mohan',20,'M',2000,'ni'
# )
# """
#
# try:
#     #执行sql语句
#     cursor.execute(sql)
#     db.commit()
# except:
#     #Rollback in case there is an error
#     db.rollback()
#
# #关闭数据库连接
# db.close()


# # 使用cursor()获取操作游标
# cursor = db.cursor()
#
# # SQL 查询语句
# sql = "SELECT * FROM EMPLOYEE  \
#       WHERE INCOME > '%d'" % (1000)
#
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         zhenshi = row[5]
#
#         # 打印结果
#         print "fname=%s,lname=%s,age=%d,sex=%s,income=%d,zhenshi=%s" % \
#               (fname, lname, age, sex,income, zhenshi)
# except:
#     print "Error：unable to fetch data"
#
# # # 执行SQL语句
# # cursor.execute(sql)
# # # 获取所有记录列表
# # results = cursor.fetchall()
# # for row in results:
# #     fname = row[0]
# #     lname = row[1]
# #     age = row[2]
# #     sex = row[3]
# #     income = row[4]
# #     zhenshi = row[5]
# #
# #     # 打印结果
# #     print "fname=%s,lname=%s,age=%d,sex=%s,income=%d,zhenshi=%s" % \
# #           (fname, lname, age, sex.income, zhenshi)
#
# # 关闭数据库连接
# db.close()

# # 数据库更新操作
# # SQL更新语句
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 \
#       WHERE SEX = '%c'" % ('M')
#
#
# try:
#     #执行SQL语句
#     cursor.execute(sql)
#     #提交到数据库执行
#     db.commit()
# except:
#     #发生错误时回滚
#     db.rollback()
#
# #关闭数据库连接
# db.close()

# SQL 删除语句
# sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
sql = "DELETE FROM EMPLOYEE WHERE AGE > 20"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭连接
db.close()
