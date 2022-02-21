def average():
    from config import average_sizes

    number_of_averages = len(average_sizes)

    for x in range(number_of_averages):
        average_size = average_sizes[x]
        with open("times.txt", "r+") as times:
            times_list = times.readlines()
            times.close()
            times_number = len(times_list)

        if times_number >= int(average_size):

            total = []
            for i in range(1, average_size + 1):
                time = times_list[-i].split(" ")[1]
                total.append(float(time))

            total.remove(min(total))
            total.remove(max(total))

            average = 0
            for i in range(average_size -2):
                average += total[i]
                
            average /= average_size - 2

            #converts it to format 00:00.00
            minutes = int(average/60)
            seconds = round(average%60, 3)

            if minutes > 0:
                if seconds > 9:
                    average = str(minutes) + ":" + str(seconds)
                    
                else:
                    average = str(minutes) + ":0" + str(seconds)

            else:
                average = round(average, 3)

            with open("times.txt", "w") as times:
                times_list[times_number-1] = times_list[times_number-1].replace("\n", "")
                times_list[times_number-1] += " Ao" + str(average_size) + " " + str(average) + "\n"
                times.writelines(times_list)
            print(f"Ao{average_size} {average}")

def print_average():
    from config import average_sizes

    number_of_averages = len(average_sizes)

    for x in range(number_of_averages):
        average_size = average_sizes[x]
        with open("times.txt", "r+") as times:
            times_list = times.readlines()
            times.close()
            times_number = len(times_list)

        if times_number >= int(average_size):

            total = []
            for i in range(1, average_size + 1):
                time = times_list[-i].split(" ")[1]
                total.append(float(time))

            total.remove(min(total))
            total.remove(max(total))

            average = 0
            for i in range(average_size -2):
                average += total[i]
                
            average /= average_size - 2

            #converts it to format 00:00.00
            minutes = int(average/60)
            seconds = round(average%60, 3)

            if minutes > 0:
                if seconds > 9:
                    average = str(minutes) + ":" + str(seconds)
                    
                else:
                    average = str(minutes) + ":0" + str(seconds)

            else:
                average = round(average, 3)
            print(f"    Ao{average_size} {average}")
