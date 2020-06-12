import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

fh = open('demo.txt', 'w')
fh.write('hallo ik ben kees')
fh.close()

sender_email = 'wicky_bhaggoe@hotmail.com'
rec_email = 'bart@crownstone.rocks'
password = 'eeenpassword'
subject = 'bijlage versturen'
body = 'dit is de bijlage die verstuurd wordt'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = rec_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

filename = 'demo.txt'
attachment = open(filename,'r')

part = MIMEBase('application', "plain")
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment, filename= "demo.txt" ')

msg.attach(part)

server = smtplib.SMTP("smtp.live.com",587)
server.starttls()
server.login(sender_email, password)
print('login was a succes')
server.sendmail(sender_email, rec_email, msg.as_string())
print('mail has been sent to', rec_email)
