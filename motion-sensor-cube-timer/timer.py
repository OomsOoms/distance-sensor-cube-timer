import time
from config import average_size, function_name, delay
from average_calculator import average
from distance_sensor import distance

timer_input = function_name

while True:
    timer_input = function_name
    
    if timer_input:
        print("Ready")
        time.sleep(delay)
        timer_input = function_name
        
        if timer_input:
            print("go")
            start = time.perf_counter()
            time.sleep(delay)
            
            while True:
                timer_input = function_name
                if timer_input:
                    stop = time.perf_counter()
                    solve = stop - start
                    solve -= delay
                    solve = round(solve, 3)
                    print(solve)
                    
                    with open("times.txt", "r") as times:
                        times_list = times.readlines()
                        times_number = len(times_list)
                
                    with open("times.txt", "a") as times:
                        times.writelines(f"{times_number}. {solve}\n")
                    average()

                    time.sleep(1)
                    break
                        
        
