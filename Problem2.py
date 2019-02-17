# Problem 2 solution

# import builtins
import random
import datetime
# create data set
data_set = []
for i in range(1, 33):
    entry = []
    for j in range(1, 17):
        single_entry = random.random()
        entry.append(single_entry)

    data_set.append(entry)
# store generated dataset to file, append mode
f = open('dataset.txt', 'a')
f.write('Data Set Generation Time: ' + str(datetime.datetime.now()) + '\n')
f.write(str(data_set) + '\n\n')
f.close()