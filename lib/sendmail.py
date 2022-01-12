from config import setting
import smtplib
from lib.newReport import new_report
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    # 发送附件
    con = configparser.ConfigParser()
    con.read(setting.TEST_CONFIG, encoding='utf-8')
    report = new_report(setting.TEST_REPORT)
    sendfile = open(report, 'rb').read()

    # --------- 读取config.ini配置文件 ---------------
    HOST = con.get("user", "HOST_SERVER")
    SENDER = con.get("user", "FROM")
    RECEIVER = con.get("user", "TO")
    USER = con.get("user", "user")
    PWD = con.get("user", "password")
    SUBJECT = con.get("user", "SUBJECT")

    att = MIMEText(sendfile, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header("Content-Disposition", "attachment", filename=("gbk", "", report))

    msg = MIMEMultipart('related')
    msg.attach(att)
    msgtext = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msgtext)
    msg['Subject'] = SUBJECT
    msg['from'] = SENDER
    msg['to'] = RECEIVER

    try:
        server = smtplib.SMTP()
        server.connect(HOST)
        server.starttls()
        server.login(USER, PWD)
        server.sendmail(SENDER, RECEIVER, msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as  e:
        print("失败: " + str(e))


if __name__ == '__main__':
    a = r'D:\1dth\Project\dth_api\report'
    report = new_report(setting.TEST_REPORT)
    send_mail(report)
