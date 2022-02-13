import RPi.GPIO as GPIO
GPIO.setwarnings(False)

from distance_sensor import distance
import time

while True:
    go = 1
    dist = distance()
    if dist < 30:
        print("Ready!")
        time.sleep(1)
        dist = distance()
        if dist < 30:
            print("GO!")
            check = 1
            while check == 1:
                dist = distance()
                if dist > 30:
                    print("Solve")
                    start = time.perf_counter()
                    time.sleep(1)
                    while go == 1:
                        dist = distance()
                        if dist < 30:
                            go = 0
                            check = 0
                            stop = time.perf_counter()
                            solve = (stop-1-start)
                            print(solve)
                            time.sleep(1)
