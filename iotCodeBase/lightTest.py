import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    GPIO.output(2,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(3,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(4,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(2,GPIO.LOW)
    GPIO.output(3,GPIO.LOW)
    GPIO.output(4,GPIO.LOW)
    time.sleep(1)