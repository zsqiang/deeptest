from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
# 输入 Email 地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入 SMTP 服务器地址:
smtp_server = input('SMTP server: ')
#构造 MIMEText 对象，第一个参数是邮件正文，第二个参数是MIME 的 subtype，传入'plain'表示纯文本，最终的 MIME 就是'text/plain'，最后一定要用 utf-8 编码保证多语言兼容性
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python 爱好者 <%s>' % from_addr)
#msg['To']接收的是字符串而不是 list，如果有多个邮件地址，用,分隔
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自 SMTP 的问候„„', 'utf-8').encode()
server = smtplib.SMTP(smtp_server, 25)
#set_debuglevel(1)打印出和 SMTP 服务器交互的所有信息
server.set_debuglevel(1)
#登录 SMTP服务器
server.login(from_addr, password)
#由于可以一次发给多个人，所以传入一个 list，邮件正文是一个 str， as_string()把 MIMEText 对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

