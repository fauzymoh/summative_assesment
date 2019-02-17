# Problem 1 solution

import random
data_set = []
for i in range(1, 33):
    entry = []
    for j in range(1, 17):
        single_entry = random.random()
        entry.append(single_entry)

    data_set.append(entry)

print('Generated Dataset: ',data_set)