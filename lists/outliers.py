data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# del data[0:2]
# print(data)
# This next del wont work as we've already removed 2 index positions
# del data[16:]
# print(data)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# The following code wont work - we are changing the size of the object we are iterating over!
# The values at index positions will change during the loop!
# The following solves that, but another way is to iterate backwards, that way removing something doesnt affect index
for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        del data[index]

print(data)

# Lets do it better this time
data2 = [4, 5, 104, 105, 110, 120, 130, 130, 150,
         160, 170, 183, 185, 187, 188, 191, 350, 360]

# process the low values in the list
stop = 0
for index, value in enumerate(data2):
    if value >= min_valid:
        stop = index
        break

print("The stop index is {}".format(stop))
del data2[:stop]
print(data2)

# Now process the high values in the list
start = 0
for index in range(len(data2) -1, -1, -1):
    if data2[index] <= max_valid:
        start = index + 1 # we have index of last item to keep, set start to position of first item to delete
        break
print(start)
del data2[start:]
print(data2)
