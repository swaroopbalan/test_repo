import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('very happy to write the mail')
msg['To'] = email.utils.formataddr(('ramya', 'v.ramyanaidu.v@gmail.com'))
msg['From'] = email.utils.formataddr(('ramyanaidu', 'ramyanaidu1458@gmail.com'))
msg['Subject'] = 'test mail'

print "hi"
server = smtplib.SMTP('mail')
print "hello"
server.set_debuglevel(True) # show communication with the server
print "good morning"
try:
    print "before sending mail"
    server.sendmail('ramyanaidu1458@gmail.com', ['v.ramyanaidu.v@gmail.com'], msg.as_string())
    print "sent mail"
finally:
    server.quit()
