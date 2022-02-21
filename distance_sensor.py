# https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
# I have edited the code since i copied it from the website

# Libraries
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
 
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
# set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
    # imports settings from config file
    from config import activation_distance
    # set Trigger to HIGH
    
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
 
    distance =  (TimeElapsed * 34300) / 2

    return distance < activation_distance
