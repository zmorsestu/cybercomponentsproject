import os
import glob
import picamera
import RPi.GPIO as GPIO
import smtplib
import boto3
from time import sleep

DIR = './Visitors/'
prefix = 'image'
            
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

session = boto3.Session( #create session with keys, may need to be changed if outdated
    aws_access_key_id="AKIAW3T63HVTVY347BNM", #access key ID
    aws_secret_access_key="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", #Secret access key
    )

def send_aws(filename):
    s3 = session.client("s3")

    s3.upload_file(
    Filename=filename, #filepath of file you're uploading
    Bucket="cybersystemsandcomponentsproject", #bucket it's going in
    Key=filename, #filename in bucket
    )
    print("Upload Complete!")

def capture_img(channel):
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
    send_aws(filename)
    
GPIO.add_event_detect(17,GPIO.RISING,callback=capture_img)

