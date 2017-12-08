#这两个包居然是自带的，怪不得pip上没有合适版本
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import time


mail_host="smtp.163.com"
mail_user="sigismundwu"
mail_pwd="********"
mail_postfix="163.com"
mail_user_name="BingcongWu"

def send_mail(send_to, sub, content):
    send_from = mail_user_name+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg["Subject"] = sub
    msg["From"] = send_from
    msg["to"] = send_to

    try:
        stp = smtplib.SMTP()
        stp.connect(mail_host)
        stp.login(mail_user, mail_pwd)
        stp.sendmail(send_from, send_to, msg.as_string())
        stp.close()
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    sub = "test" #这个sub是邮件的头
    content = "hello world!" #content在这个地方改，可以有很多个，这个要看你需要了
    #然后整个程序定义的函数就那一个
    mailto_list = ["sigismundwu@163.com", "wubingcong.1015@gmail.com"]
    for i in mailto_list:
        if send_mail(i,sub, content):
            print("good")
        else:
            print("bad")






