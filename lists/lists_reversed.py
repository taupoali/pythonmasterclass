my_list =[20, 23, 44, 2, 5]
print(my_list)
print(type(my_list))
print(enumerate(my_list))
# The result of printing return value of enumerate is just an enumerate object
# The enumerate object is an iterable
for a,b in enumerate(my_list):
    print(a,b)

my_list_reverse_iterator = reversed(my_list)
print(type(my_list_reverse_iterator))
print(my_list_reverse_iterator)
# the result of reversed is list_reverseiterator object so we can't print it

# The list() constructor returns a list.
# If no parameters are passed, it returns an empty list
# If iterable is passed as a parameter, it creates a list consisting of iterable's items.
# In the following we are passing the reverse_iterator as a parameter

print(list(my_list_reverse_iterator))