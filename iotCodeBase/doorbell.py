import os
import glob
###import picamera
###import RPi.GPIO as GPIO
import smtplib
from time import sleep

###from email.MIMEMultipart import MIMEMultipart
###from email.MIMEText import MIMEText
###from email.MIMEBase import MIMEBase
from email import encoders

sender = 'parkoff@student.uiwtx.edu'
password = '***************'
receiver = 'parkoff@student.uiwtx.edu'

DIR = './Visitors/'
prefix = 'image'
            
###GPIO.setwarnings(False)
###GPIO.setmode(GPIO.BOARD)
###GPIO.setup(15, GPIO.IN)  

def send_mail(filename):
    ###msg = MIMEMultipart()
    ###msg['From'] = sender
    ###msg['To'] = receiver
    ###msg['Subject'] = 'Visitor'
    
    body = 'Find the picture in attachments'
    ###msg.attach(MIMEText(body, 'plain'))
    attachment = open(filename, 'rb')
    ###part = MIMEBase('application', 'octet-stream')
    ###part.set_payload((attachment).read())
    encoders.encode_base64(part)
   ## part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
   ## msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    ###text = msg.as_string()
    ###server.sendmail(sender, receiver, text)
    server.quit()

def capture_img():
    print ('Capturing')
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    files = sorted(glob.glob(os.path.join(DIR, prefix + '[0-9][0-9][0-9].jpg')))
    count = 0
    
    if len(files) > 0:
        count = int(files[-1][-7:-4])+1
    filename = os.path.join(DIR, prefix + '%03d.jpg' % count)
    ###with picamera.PiCamera() as camera:
       ### pic = camera.capture(filename)
    send_mail(filename)

while True:
       ##if in== GPIO.input(11):
        ##if == 0:
        print('Waiting'),i 
        sleep(0.4)
##elif == 1:  
    ##print('Captured');"Sending", i
    ###capture_img()