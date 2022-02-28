import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr



class sendMail:
    '''
    发送邮件模块
    '''
    def __init__(self):
        # 第三方邮件smtp服务器
        self.mail_host = 'smtp.163.com'
        # 邮件发送方和接收方
        self.sender = 'playgm@163.com'
        # 接收方可以是多个
        self.receivers = ['196185996@qq.com']

    def _format_addr(self,s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send_mail(self,msg,msg_title):
        # 实例化邮件对象
        message = MIMEText(msg,'plain','utf-8')

        # 发件人的名字
        message['From'] = self._format_addr('发送端<%s>' % self.sender)
        # 收件人的名字
        message['To'] = self._format_addr('接收端<%s>' % self.receivers)
        # 邮件的标题
        subject = msg_title
        message['Subject'] = Header(subject, 'utf-8')

        # 使用网易邮箱服务器发送邮件
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.sender, 'YYNXFSMWUJKLQZFG')
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            smtpObj.quit()
            print("邮件发送成功")
        except smtplib.SMTPException:
            smtpObj.quit()
            print("Error: 无法发送邮件")

mt = sendMail()


if __name__ == '__main__':
    m = sendMail()
    m.send_mail()




