times = open("times.txt", "r+")
times_list = times.readlines()
times_number = len(times_list)

times_list = []
for i in range(len(times_list)-1):
    times_list.append(times_list[i] - times_list[i+1])
    
print(times_list)