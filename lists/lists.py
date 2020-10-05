# This isnt like ordinary assignment of value to variable
# You have two variable names pointing at same memory!
list1 = [1,2,3,4,5]
print(list1)
list2 = list1
print(list2)
list2.append(6)
print(list1)
