import RPi.GPIO as GPIO
import time

def button_press(channel):
    channel = GPIO.wait_for_edge(channel, GPIO.RISING, timeout=1500)
    if channel is None:
        print('LED 1')
    else:
        channel = GPIO.wait_for_edge(channel, GPIO.RISING, timeout=1500)
        if channel is None:
            print('LED 2')
        else:
            channel = GPIO.wait_for_edge(channel, GPIO.RISING, timeout=1500)
            if channel is None:
                print('LED 3')
                time.sleep(3)
            else:
                print('Too many button presses!')
                time.sleep(3)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(17,GPIO.RISING,callback=button_press,bouncetime=8000) # Setup press event on pin 17

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up