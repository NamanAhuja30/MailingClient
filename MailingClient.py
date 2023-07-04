import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


#creating a multipart message object
main = MIMEMultipart()

# Setting the sender , recipient and sujbect
main['From'] = 'Senders-detail'
main['To'] = 'Receivers-detail'
main['Subject'] = 'Damn it worked !'


#Adding plain text part
with open('textPart.txt','r') as f:
    textMsg = f.read()

textPart = MIMEText(textMsg , 'plain')
main.attach(textPart)



#Adding an attachment to the message
# Image credits : https://wallpaperaccess.com/american-psycho-hd

attachment = open('image.jpg','rb')
attachmentPart = MIMEBase('application','octet-stream')
attachmentPart.set_payload(attachment.read())
attachment.close()
encoders.encode_base64(attachmentPart)
attachmentPart.add_header('Content-Disposition','attachment',filename='image.jpg')
main.attach(attachmentPart)


#converting the message to string
msgString = main.as_string()


#creating an SMTP session
server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls() 

with open('AppPassword.txt','r') as f:  #using an APP PASSWORD gor gmail account
    password = f.read()

with open('senderId.txt','r') as f:
    senderId = f.read()

with open('receiverId.txt','r') as f:
    receiverId = f.read()

server.login(senderId,password)

server.sendmail(senderId,receiverId,msgString)

server.quit()

