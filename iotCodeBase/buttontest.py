import RPi.GPIO as GPIO
import time

def button_callback(channel):
    print("Button was pushed!")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(17,GPIO.RISING,callback=button_callback) # Setup event on pin 17 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up