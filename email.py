import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

fh = open('demo.txt', 'w')
fh.write('hallo ik ben kees')
fh.write('ik ben 15 jaar oud')
fh.close()

def sendMail(sender_email, rec_email, password, sbject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = rec_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    attachment = open(filename)

    part = MIMEBase('application', "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {filename}')

    msg.attach(part)

    server = smtplib.SMTP("smtp.live.com",587)
    server.starttls()
    server.login(sender_email, password)
    print('login was a succes')
    server.sendmail(sender_email, rec_email, msg.as_string())
    print('mail has been sent to', rec_email)
