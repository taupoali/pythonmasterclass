import timeit

# The longer code as we saw in outliers has 2 loops and looks more complicated - more lines of code
# But it uses slicing to delete in batch - which is only possible as this particular list is already SORTED
# With the gobackwards methods, when we delete, its a single item and we shuffle down on the indexing
# With large lists, this is significantly slower! 0.6s vs 9s

max_value = 100
min_valid = 10
max_valid = 97

data_list1 = list(range(max_value))
data_list2 = list(range(max_value))
data_list3 = list(range(max_value))

def sanitise_1(data):
    stop = 0
    for index

sanitise_1(data_list1)
print(data_list1)
sanitise_2