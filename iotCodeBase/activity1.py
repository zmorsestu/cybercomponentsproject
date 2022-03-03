import RPi.GPIO as GPIO
import time

def button_callback(channel):
    while True:
        input_value = GPIO.input(18)

        if input_value == True:
            pressed += 1;
            time = 0; #to start the counter at 0

        if (time > 10): #you wait 1 sec between each presure
            print("the button has been pressed " + pressed + " times");
            pressed = 0; # you don't count anymore

        if (pressed > 0): # you are pressing the button so you count
            time += 1;

        time.sleep(0.1)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(17,GPIO.RISING,callback=button_callback) # Setup event on pin 17 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up