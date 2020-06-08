import smtplib
import pandas as pd
import numpy as np
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#untuk login
#email_sender = 'tubessister19@gmail.com'
#email_password = 'sister2019'
#email_receiver ='hovelywahyu@student.telkomuniversity.ac.id'

email_sender =input('type your email : ')
email_password =input('type your password : ')

try:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_sender,email_password)
    print("LOGIN BERHASIL")

    email_receiver =input('SEND TO :')
    #test.txt /// gambar.jpeg /// 1301164167 Registrasi _ Telkom University.pdf
    filename =input('FILENAME :')
    subject =input('SUBJECT :')
    body =input('TEXT BODY :')

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= " +filename)

    msg.attach(part)
    text = msg.as_string()

    try:
        #server.login(email_sender,email_password)
        server.sendmail(email_sender,email_receiver,text)

        print("BERHASIL")
        server.quit()
    except:
        print("GAGAL")
except:
    print("LOGIN GAGAL")




