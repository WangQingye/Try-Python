from email.mime.text import MIMEText
from info import *
import smtplib

mail_list = ["5983495@qq.com"]
mail_host = "smtp.qq.com"
mail_user = "329103586"
mail_pass = "gqfumcntovhfbjgc"
mail_postfix = "qq.com"


def send_mail(to_list, sub, content):
    me = "LoverW" + (day-68) + "<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content.encode('utf-8'), 'plain', 'utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    try:
        s = smtplib.SMTP_SSL(mail_host, 465)
        s.set_debuglevel(1)
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mail_list, 'text1', content):
        print "done"
    else:
        print "wrong"
