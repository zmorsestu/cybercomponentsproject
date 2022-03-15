import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#setup LED pinout
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
#setup button pinout
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#create a callback for when the button is pressed
def button_callback(channel):
    print("Button was pushed!")

#using GPIO events, do this callback when the button is pressed
GPIO.add_event_detect(17,GPIO.RISING,callback=button_callback)

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up