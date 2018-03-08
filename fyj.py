import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.application import MIMEApplication
import datetime
  
sender = '909355014@qq.com'  
receiver = '909355014@qq.com'  
smtpserver = 'smtp.qq.com'  
username = '909355014@qq.com'  
password = 'muhydfatrcblbegf'
name = 'wechatlogin.png'
  
msg = MIMEMultipart()  
msg['Subject'] = name
msg['From'] = 'wechatlogin'
msg['To'] = 'you'
text = MIMEText('请接收'+ name+'!','plain','utf-8')

msg.attach(text)


  
#构造附件
def fsyj():
    loginpng = MIMEApplication ( open( name,'rb').read(),'base64')
    loginpng.add_header('Content-Disposition','attachment',filename = name )
    msg.attach(loginpng)
    smtp = smtplib.SMTP_SSL(smtpserver,465)  
    smtp.login(username, password)  
    smtp.sendmail(sender, receiver.split(','), msg.as_string())  
    smtp.quit() 
if __name__=='__main__':
    fsyj()
