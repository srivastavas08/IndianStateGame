# Python code to illustrate Sending mail with attachments 
# from your Gmail account  

# libraries to be imported 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_addr = "mongoengine@gmail.com"
password = "SHIvam7426"
to_addr = "mongoengine@gmail.com"

# instance of MIMEMultipart 
msg = MIMEMultipart()

# storing the senders email address   
msg['From'] = from_addr

# storing the receivers email address  
msg['To'] = to_addr

# storing the subject  
msg['Subject'] = "STATES YOU NEED TO LEARN"

# string to store the body of the mail 
body = "Hey There!\n \n I am attaching the file with the list of names you need to learn\n \n \n Thanks and Regards\n Python"

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent  
filename = "States.csv"
attachment = open("States.csv", "rb")

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form 
p.set_payload(attachment.read())

# encode into base64 
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg' 
msg.attach(p)

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security 
s.starttls()

# Authentication 
s.login(from_addr, password)

# Converts the Multipart msg into a string 
text = msg.as_string()

# sending the mail 
s.sendmail(from_addr, to_addr, text)

# terminating the session 
s.quit()
