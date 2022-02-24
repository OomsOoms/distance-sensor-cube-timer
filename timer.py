# checking if using Rpi.gpio module
try:
    from config_sensor import delay, function_name, input_method
    from distance_sensor import distance
except ModuleNotFoundError or NameError:
    delay = 0
    input_method = 0
    reset = open("config.py", "w")
    reset.write("\n")
    reset.write("delay = 1\n")
    reset.write("activation_distance = 30\n")
    reset.write("average_sizes = [5,12,25]\n")
    reset.write("\n")
    reset.write("input_method = 0\n")
    reset.close()
    print("No sensor detected, sensor files deleted, open the settings menu and select option 5 to reset")

# importing modules    
import time
from average_calculator import average, print_average

# timer code
while True:
    try:
        if input_method == 1:
            while True:
                ready = False
                while True:
                    if ready:
                        function_name()
                        if not function_name():
                            ready = False
                            print("Solve")
                            start = time.perf_counter()
                            time.sleep(delay)
                                        
                            while True:
                                function_name()
                                if function_name():
                                    stop = time.perf_counter()
                                    solve = stop - start
                                    solve -= delay
                                    solve = round(solve, 3)
                                    print(solve)
                                                
                                    with open("times.txt", "r") as times:
                                        times_list = times.readlines()
                                        times_number = len(times_list) +1
                                                
                                    with open("times.txt", "a") as times:
                                        times.writelines(f"{times_number}. {solve}\n")
                                    average()
                                    time.sleep(3)
                                    
                                    break
                    else:
                        input_method == 1
                        time.sleep(delay)
                        print("ready")
                        ready = True

        if input_method == 0:

            input()
            print("Solve")
            start = time.perf_counter()             
            input()
            stop = time.perf_counter()
            solve = stop - start
            solve -= delay
            solve = round(solve, 3)
            print(solve)
                                    
            with open("times.txt", "r") as times:
                times_list = times.readlines()
                times_number = len(times_list) +1
                                    
            with open("times.txt", "a") as times:
                times.writelines(f"{times_number}. {solve}\n")
            average()
            
    except KeyboardInterrupt:
            print("""\n    -------------Menu-------------\n
    1 - Change input\n
    2 - Print current solve\n
    3 - Print current solve number\n
    4 - Print current average\n
    5 - Edit config file\n
    6 - Print all saved times\n
    7 - Delete last solve\n
    8 - Reset config\n
    9 - Exit\n""")

            menu = 1
            while menu == 1:
                print("    Pick an option\n")

                try:
                    option = int(input("    "))
                    
                    # option 1
                    if option == 1:
                        print("    Enter 1(sensor, if connected) or 0 (enter key)")
                        if input_method == 1:
                            edit = open("config.py", "w")
                            l6 = option = int(input("    "))
                            edit.write(l1)
                            edit.write(l2)
                            edit.write(l3)
                            edit.write(l4)
                            edit.write(l5)
                            edit.write(l6)
                            edit.close()
                        else:
                            ("No sensor connected")
                            
                    # option 2
                    elif option == 2:
                        try:
                            print("    " + solve)
                        except NameError:
                            print("    You havent done a solve yet")

                    # option 3
                    elif option == 3:
                        with open("times.txt", "r") as times:
                            times_list = times.readlines()
                            times_number = len(times_list)
                        print("    " + str(times_number))

                    # option 4
                    elif option == 4:
                        print_average()

                    # option 6
                    elif option == 6:
                        with open("times.txt", "r") as times:
                            times_list = times.readlines()
                        print(times_list)

                    # option 7
                    elif option == 7:
                        fd=open("times.txt","r")
                        d=fd.read()
                        fd.close()
                        m=d.split("\n")
                        s="\n".join(m[:-1])
                        fd=open("times.txt","w+")
                        for i in range(len(s)):
                            fd.write(s[i-1])
                        fd.close()
                        print("    Deleted")

                    # option 5
                    elif option == 5:
                        all_config = open("config.py", "r")
                        settings = open("config.py", "r")
                        l1 = settings.readline()
                        l2 = settings.readline()
                        l3 = settings.readline()
                        l4 = settings.readline()
                        l5 = settings.readline()
                        l6 = settings.readline()
                        print("""    Which setting do you want to change\n
    1 - delay\n
    2 - activation_distance\n
    3 - averahe sizes\n
    4 - function name\n
    5 - back <--\n""")

                        option = int(input("    "))
                        if option == 1:
                            print("    Enter value, only effects if you are using the sensor")
                            option = input("    ")
                            edit = open("config.py", "w")
                            l2 = "delay = " + option + "\n"
                            edit.write(l1)
                            edit.write(l2)
                            edit.write(l3)
                            edit.write(l4)
                            edit.write(l5)
                            edit.write(l6)
                            edit.close()
                            if sensor == 1:
                                delay = float(option)
                                                    
                            pass
                        if option == 2:
                            print("    Enter value (Seconds)")
                            option = input("    ")
                            edit = open("config.py", "w")
                            l3 = "activation_distance = " + option + "\n"
                            edit.write(l1)
                            edit.write(l2)
                            edit.write(l3)
                            edit.write(l4)
                            edit.write(l5)
                            edit.write(l6)
                            edit.close()
                            activation_distance = float(option)
                                                    
                            pass
                        if option == 3:
                            print("    Enter value, seperate each number by a comma")
                            option = input("    ")
                            edit = open("config.py", "w")
                            l4 = "average_sizes = " + "[" + option + "]" + "\n"
                            edit.write(l1)
                            edit.write(l2)
                            edit.write(l3)
                            edit.write(l4)
                            edit.write(l5)
                            edit.write(l6)
                            edit.close()
                            average_sizes = "[" + option + "]"
                                                    
                            pass
                        if option == 4:
                            print("    Enter name")
                            option = input("    ")
                            edit = open("config.py", "w")
                            l5 = "function_name = " + option + "\n"
                            edit.write(l1)
                            edit.write(l2)
                            edit.write(l3)
                            edit.write(l4)
                            edit.write(l5)
                            edit.write(l6)
                            edit.close()
                            function_name = option
                                                    
                            pass
                        if option == 5:
                            pass

                    # option 8
                    elif option == 8:
                        reset = open("config.py", "w")
                        reset.write("from distance_sensor import distance\n")
                        reset.write("delay = 1\n")
                        reset.write("activation_distance = 30\n")
                        reset.write("average_sizes = [5,12,25]\n")
                        reset.write("function_name = distance\n")
                        reset.write("input_method\n")
                        reset.close()

                    # option 9 
                    elif option == 9:
                        menu = 0
                        print("    exiting\n")
                        time.sleep(1)
                        pass

                    else:
                        print("    Not an option")

                except ValueError:
                     print("    Type a number")
