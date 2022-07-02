import smtplib
from email.mime.text import MIMEText

def send_messega(title,messageq):
    smtp_server = 'smtp.163.com'	# STMP邮箱服务器地址
    smtp_user = '@163.com'	# 用户名
    smtp_passwd = ''# 授权码，需要到邮箱里面开启STMP服务，然后会给一个授权码
    sender = '@163.com'		# 发送者邮箱
    receivers  = ['@qq.com','@qq.com'] # 接收者邮箱，可以写多个

    message = MIMEText(messageq,'plain','utf-8')# 第一个为文本内容，第二个设置文本格式，第三个utf-8设置编码
    message['Subject'] = title	# 邮件标题
    message['From'] = sender	# 发送者
    message['To'] = receivers[0]# 接收方

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(smtp_server,25)
        smtpObj.login(smtp_user,smtp_passwd)
        smtpObj.sendmail(sender,receivers,message.as_string())
        smtpObj.quit()
        print('发送成功')
    except smtplib.SMTPException as e:
        print('发送错误')