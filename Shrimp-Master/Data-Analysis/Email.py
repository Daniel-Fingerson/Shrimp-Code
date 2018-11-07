from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib

#send to email when it is going over data
def email(filename,threshold):
    #IN PROGRESS!!!!
    froma = "16lucmendez@asfg.edu.mx"
    toa = "djfingerson@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = froma
    msg['To'] = toa
    msg['Subject'] = "Oxygen Levels Rising"

    body="Oxygen levels over %d"%(threshold)
    msg.attach(MIMEText(body,'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()   
    server.starttls()
    server.ehlo()
    server.login("16lucmendez@asfg.edu.mx",XXXXXX)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
