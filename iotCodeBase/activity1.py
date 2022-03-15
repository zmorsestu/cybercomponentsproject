import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    channel = GPIO.wait_for_edge(17, GPIO.RISING, timeout=1500)
    if channel is None:
        print('LED OFF')
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.HIGH)
    else:
        channel = GPIO.wait_for_edge(17, GPIO.RISING, timeout=1500)
        if channel is None:
            print('LED 1')
            GPIO.output(2,GPIO.LOW)
        else:
            channel = GPIO.wait_for_edge(17, GPIO.RISING, timeout=1500)
            if channel is None:
                print('LED 2')
                GPIO.output(3,GPIO.LOW)
            else:
                channel = GPIO.wait_for_edge(17, GPIO.RISING, timeout=1500)
                if channel is None:
                    GPIO.output(4,GPIO.LOW)
                    print('LED 3')
                    time.sleep(1)
                else:
                    print('Too many button presses!')
                    time.sleep(3)

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up