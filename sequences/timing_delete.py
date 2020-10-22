# import timeit

# The longer code as we saw in outliers has 2 loops and looks more complicated - more lines of code
# But it uses slicing to delete in batch - which is only possible as this particular list is already SORTED
# With the go backwards methods, when we delete, its a single item and we shuffle down on the indexing
# With large lists, this is significantly slower! 0.6s vs 9s

max_value = 100
min_valid = 10
max_valid = 97

data_list1 = list(range(max_value))
data_list2 = list(range(max_value))
data_list3 = list(range(max_value))


def sanitise_1(data):
    stop = 0
    for index, value in enumerate(data):
        if value >= min_valid:
            stop = index
            break
    del data[:stop]

    start = 0
    for index in range(len(data) -1, -1, -1):
        if data[index] <= max_valid:
            start = index + 1
            break
    del data[start:]









def sanitise_2(data):
    stop = 0


def sanitise_3(data):
    stop = 0


sanitise_1(data_list1)
print(data_list1)
sanitise_2(data_list2)
print(data_list2)
sanitise_3(data_list3)
print(data_list3)
