from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import time
import random


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = ''
password = ''
smtp_server = ''
email_list = open('teacher.txt', 'r')
for line in email_list:
    time.sleep(20)
    email = line.strip().split('\t')
    if len(email) > 2:
        curtime = time.localtime()
        number = random.random()
        msg = MIMEText(f'尊敬的{email[1]}老师：\n\r'
                       f'\t您好！本封邮件为Python爬虫自动发送，如有打扰请您谅解，预祝您春节快乐，工作顺利！\n\r\n\r'
                       f'\n\r'
                       f'2019-1-11 {curtime.tm_hour}:{curtime.tm_min}:{curtime.tm_sec}\n\r', 'plain', 'utf-8')
        msg['From'] = _format_addr(f'Python <{from_addr}>')
        msg['To'] = _format_addr(f'{email[1]} <{email[2]}>')
        msg['Subject'] = Header(f'{email[1]}老师您好！', 'utf-8').encode()
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [email[2]], msg.as_string())
        server.quit()
