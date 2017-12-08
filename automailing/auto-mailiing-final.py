#这两个包居然是自带的，怪不得pip上没有合适版本
import smtplib
from email.mime.text import MIMEText
import time


mail_host="smtp.163.com" #你发邮件的邮箱的smtp
mail_user="sigismundwu" #你的邮箱登录名
mail_pwd="**********" #你的邮箱登录密码
mail_postfix="163.com" #邮箱后缀，在@后面的部分
mail_user_name="BingcongWu" #邮箱名字（这个写不写都可以的）

def send_mail(send_to, sub, content):
    send_from = mail_user_name+"<"+mail_user+"@"+mail_postfix+">" #构建一个用户名
    msg = MIMEText(content) #解析主函数中你要发送的内容的
    msg["Subject"] = sub #sub是主题
    msg["From"] = send_from #From就是发件人地址，上面刚定义那个
    msg["to"] = send_to #收件人地址

    try:
        stp = smtplib.SMTP() #生成SMTP对象
        stp.connect(mail_host) #用连接方法，就是上面提到的那些
        stp.login(mail_user, mail_pwd) #登录信息
        stp.sendmail(send_from, send_to, msg.as_string()) #发送方法
        stp.close() #关闭发送进程
        return True
    except Exception as e:
        print(e) #有任何错误会打印出来，通知使用者
        return False

if __name__ == "__main__":
    sub = {
        "2017/12/6/19/59/59":"good",
        "2017/12/6/20/0/59":"so good" #正常日期肯定不是这样写，这样写是为了方便字符串切割，反正程序规则是开发者定的
        # 而且非要弄成正规的也不是，正则表达式即可，但是比较懒。。。嫌麻烦，作为一个小程序，没必要
    } #这个sub是邮件的头
    #这个sub的话，可以按照content一样做成字典，但是因为是test，我就懒得写了
    #注意sub邮件的头，时间必须和下面content的一一匹配
    content = {
        "2017/12/6/19/59/59":"good",
        "2017/12/6/20/0/59":"so good"
    } #content在这个地方改，可以有很多个，这个要看你需要了
    #然后整个程序定义的函数就那一个
    mailto_list = ["sigismundwu@163.com", "wubingcong.1015@gmail.com"] #发送的列表
    #通过下面的for循环发送给每个人（这个看你需要可以添加多个，这个甚至可以加个input函数让使用者输入）
    #当然要做一个带input你上面的也要修改
    #localtime,抓取系统时间
    #这个localtime返回本质的是一个tuple，切片方式如下：
    #0：年，1：月，2：日，3：小时，4：分钟，5：秒
    countlist = []
    while True:
        time.sleep(1)#每一秒，这个while True循环会被执行一次，抓取localtime之后判断是否发送
        #每隔一秒一次的话，性能也接受得了，就像一般时钟计时一样，就算是我的这个破笔记本都没压力
        localtime = time.localtime()
        localtime = list(localtime)[0:6]
        print(localtime)
        if len(content) > len(countlist): #当你的字典里还有没发送的东西的时候，就能用
        #我在测试这里用的是基于一个规则：当年月日小时秒都相同的时候，隔一分钟发一次
            for k,v in content.items():
                if localtime == list((map(int,k.split("/")))):
                    for i in mailto_list:
                        if send_mail(i,sub[k], v):#这边sub[k]就是上面sub和content内容一定要一致的原因
                            print("sent")
                        else:
                            print("bad")
                    countlist.append(k)#通过在这个countinglist，设计好的每天事物完成了，就会自动shutdown整个服务
        else:
            print("All emails sent, service shut down")
            break

