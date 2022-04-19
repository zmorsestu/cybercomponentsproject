import os
import glob
import picamera
import RPi.GPIO as GPIO
import smtplib
import boto3
from time import sleep

#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#from email.mime.base import MIMEBase
#from email import encoders

sender = 'parkoff@student.uiwtx.edu'
password = '***************'
receiver = 'parkoff@student.uiwtx.edu'

DIR = './Visitors/'
prefix = 'image'
            
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)  

session = boto3.Session( #create session with keys, may need to be changed if outdated
    aws_access_key_id="AKIAW3T63HVT24D5MC3", #access key ID
    aws_secret_access_key="FO0z6yQhkAeRjFha+BpESM6AXI1JMFsp2kTSUpV2", #Secret access key
    )

def send_mail(filename):
    s3 = session.client("s3")

    s3.upload_file(
    Filename=filename, #filepath of file you're uploading
    Bucket="cybersystemsandcomponentsproject", #bucket it's going in
    Key=filename, #filename in bucket
    )

def capture_img():
    print ('Capturing')
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    files = sorted(glob.glob(os.path.join(DIR, prefix + '[0-9][0-9][0-9].jpg')))
    count = 0
    
    if len(files) > 0:
        count = int(files[-1][-7:-4])+1
    filename = os.path.join(DIR, prefix + '%03d.jpg' % count)
    with picamera.PiCamera() as camera:
       pic = camera.capture(filename)
    send_mail(filename)

while True:
    if (GPIO.input(11)):
        print('ON')
        sleep(0.4)
        print('Capture')
        capture_img()
    else:
        print('OFF')
        sleep (0.4)
