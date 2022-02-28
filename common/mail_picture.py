import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import time


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

    def send_mail(self,image=None,file=None):
        # 实例化邮件对象
        message = MIMEMultipart('related')

        # 发件人的名字
        message['From'] = self._format_addr('自动化薅羊毛<%s>' % self.sender)
        # 收件人的名字
        message['To'] = self._format_addr('晚饭吃什么<%s>' % self.receivers)
        now_time = time.strftime('%Y-%m-%d')
        # 邮件的标题
        subject = '自动化脚本执行成功'+now_time
        message['Subject'] = Header(subject, 'utf-8')
        # 添加附件
        msgAlternative = MIMEMultipart('alternative')
        message.attach(msgAlternative)

        mail_msg = """
        <p>Python 自动化执行结果</p>
        <p>截图展示：</p>
        <p><img src="cid:image1"></p>
        """

        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        fp = open(image, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        msgImage.add_header('Content-ID', '<image1>')
        message.attach(msgImage)

        # 使用网易邮箱服务器发送邮件
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.sender, 'YYNXFSMWUJKLQZFG')
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            smtpObj.quit()
            from common.logconf import logger
            logger.info('自动化执行结果邮件发送成功')
        except smtplib.SMTPException:
            smtpObj.quit()
            logger.error('无法正常发送邮件')
image = 'D:\\auto_task\\excute_image\\1.jpg'
mp = sendMail()

if __name__ == '__main__':
    m.send_mail(image)




