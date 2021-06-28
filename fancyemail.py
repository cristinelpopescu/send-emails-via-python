import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path(".\\index.html").read_text())


msg_header = 'From: Sender Name <"sender@gmail.com">\n' \
             'To: Receiver Name <"receiver1@yahoo.com">\n' \
             'Cc: Receiver2 Name <receiver2@server>\n' \
             'MIME-Version: 1.0\n' \
             'Content-type: text/html\n' \
             'Subject: Any subject\n'
title = 'e-mail title'
msg_content = html.substitute(names = 'Mr. Vitalik')
msg_full = (''.join([msg_header, msg_content])).encode()

server = smtplib.SMTP('smtp.gmail.com:587') #port 587 for tls, port 465 for ssl
server.starttls()
server.login = (user = 'sender@gmail.com', password = "blablabla")
server.sendmail("sender@gmail.com",
                ["receiver1@yahoo.com", 'receiver2@server.com'],
                msg_full)
server.quit()