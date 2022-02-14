import RPi.GPIO as GPIO
GPIO.setwarnings(False)

import time
from average_calculator import average_times
from config import delay, activation_distance
from distance_sensor import distance

while True:
    go = 1
    dist = distance()
    if dist < activation_distance:
        print("Ready!")
        time.sleep(delay)
        dist = distance()
        if dist < activation_distance:
            check = 1
            print("GO!")
            while check == 1:
                dist = distance()
                if dist > activation_distance:
                    print("Solve")
                    start = time.perf_counter()
                    time.sleep(1)
                    while go == 1:
                        dist = distance()
                        if dist < activation_distance:
                            go = 0
                            check = 0
                            
                            stop = time.perf_counter()
                            solve = (stop-1-start)
                            average_times()
                            print("1")
                            time.sleep(1)