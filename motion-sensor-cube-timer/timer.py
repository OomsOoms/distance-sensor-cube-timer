import time
from config import delay, function_name
from average_calculator import average, print_average
from distance_sensor import distance

while True:
    try:
        while True:
            ready = False
            while True:
                if ready:
                        
                    function_name()
                    if function_name() is False:
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
                    if function_name():
                        time.sleep(delay)
                        print("ready")
                        ready = True
    except KeyboardInterrupt:
            print("""\n    -------------Menu-------------\n
    1 - Print current solve\n
    2 - print current solve number\n
    3 - print current average\n
    4 - print all saved times\n
    5 - delete last solve\n
    6 - edit config file\n
    7 - exit\n""")

            menu = 1
            while menu == 1:
                print("    Pick an option\n")

                try:
                    option = int(input("    "))

                    if option == 1:
                        try:
                            print("    " + solve)
                        except NameError:
                            print("    You havent done a solve yet")
                        
                    elif option == 2:
                        with open("times.txt", "r") as times:
                            times_list = times.readlines()
                            times_number = len(times_list)
                        print("    " + str(times_number))

                    elif option == 3:
                        print_average()

                    elif option == 4:
                        print(times_list)

                    elif option == 5:
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
                    
                    elif option == 6:
                        all_config = open("config.py", "r")
                        settings = open("config.py", "r")
                        l1 = settings.readline()
                        l2 = settings.readline()
                        l3 = settings.readline()
                        l4 = settings.readline()
                        l5 = settings.readline()
                        print("""    Which setting do you want to change\n
    1 - delay\n
    2 - activation_distance\n
    3 - averahe sizes\n
    4 - function name\n
    5 - back <--\n""")

                        option = int(input("    "))
                        if option == 1:
                            print("    Enter value")
                            option = input("    ")
                            edit = open("config.py", "w")
                            l2 = "delay = " + option + "\n"
                            edit.write(l1)
                            edit.write(l2)
                            edit.write(l3)
                            edit.write(l4)
                            edit.write(l5)
                            edit.close()
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
                            edit.close()
                            function_name = option
                                                    
                            pass
                        if option == 5:
                            pass
                        
                    elif option == 7:
                        menu = 0
                        print("    exiting\n")
                        time.sleep(1)
                        pass

                    else:
                        print("    Not an option")

                except ValueError:
                     print("    Type a number")

        
