# -*-coding:utf-8-*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# # 本地发送邮件
# sender = 'from@runoob.comm'

# 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# receivers = ['1009924082@qq.com']
#
# # 三个参数：第一个为文本内容，第二个为plain设置文本格式，第三个utf-8设置
# message = MIMEText('Python 邮件发送测试……', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print "邮件发送成功"
# except smtplib.SMTPException as e:
#     print "Error：无法发送邮件" + str(e)


# # 第三方发送邮件（163邮箱）
# # 第三方SMTP服务
# # 设置服务器
# mail_host = "smtp.163.com"
# # 用户名
# mail_user = "knoixs@163.com"
# # 密码
# mail_passwd = "LINdls216"

# subject = 'Python SMTP 邮件测试'
#
# sender = 'knoixs@163.com'
# # 接收邮件
# receivers = ['1009924082@qq.com']
#
# message = MIMEText('Python 邮件发送测试……', 'plain', 'utf-8')
# # message['From'] = Header("菜鸟教程", 'utf-8')
# message['From'] = "knoixs@163.com"
# # message['To'] = Header("测试", 'utf-8')
# message['To'] = u'1009924082@qq.com'
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)
#     smtpObj.login(mail_user, mail_passwd)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print "邮件发送成功"
# except smtplib.SMTPException as er:
#     print "Error：无法发送邮件" + str(er)


# 创建一个带附件的实例
# message = MIMEMultipart()
# message['From'] = 'knoixs@163.com'
# message['to'] = '1009924082@qq.com'
#
# subject = 'Python SMTP 邮件车市'
# message['Subject'] = Header(subject,'utf-8')
#
# # 邮件正文内容
# message.attach(MIMEText('这是菜鸟教程Python邮件发送测试……','plain','utf-8'))
#
# #构造附件,传送当下目录的txt文件
# att1 = MIMEText(open('邮件测试附件.txt','rb').read(),'base64','utf-8')
# att1['Content-Type'] = 'application/octet-stream'
#
# #这里的filename可以任意写，写什么名字，邮件显示什么名字
# att1['Content-Disposition'] = 'attachment;filename="text.txt"'
# message.attach(att1)
#
# sender = 'knoixs@163.com'
# receivers = '1009924082@qq.com'
#
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)
#     smtpObj.login(mail_user, mail_passwd)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print "邮件发送成功"
# except smtplib.SMTPException as er:
#     print "Error：无法发送邮件" + str(er)


# 在ＨＴＭＬ文本中添加图片
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

sender = 'knoixs@163.com'
#接收邮件
receivers = ['1009924082@qq.com']

msgRoot = MIMEMultipart('related')
msgRoot['From'] = 'knoixs@163.com'
msgRoot['To'] = '1009924082@qq.com'
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject,'utf-8')

msAlternative = MIMEMultipart('alternative')
msgRoot.attach(msAlternative)

mail_host="smtp.163.com"
mail_user = "knoixs@163.com"
mail_passwd = "LINdls216"

mail_msg = """
<p>Python 邮件发送测试……</p>
<p><a href="http://runoob.com">菜鸟教程连接</a></p>
<p>图片演示:</p>
<p><img src="cid:image1"</p>
"""

msAlternative.attach(MIMEText(mail_msg,'html','utf-8'))

#指定图片为当前目录
fp = open('test.jpg','rb')
msgImage = MIMEImage(fp.read())
fp.close()

#定义图片ID,在ＨＴＭＬ文本中引用
msgImage.add_header('Content-ID','<image1>')
msgRoot.attach(msgImage)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_passwd)
    smtpObj.sendmail(sender,receivers,msgRoot.as_string())
    print "邮件发送成功"
except smtplib.SMTPException as err:
    print "Error:无法发送邮件"+str(err)