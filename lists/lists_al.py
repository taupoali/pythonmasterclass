# This isnt like ordinary assignment of value to variable
# You have two variable names pointing at same memory!
list1 = [1,2,3,4,5]
print(list1)
list2 = list1
print(list2)
list2.append(6)
print(list1)
<<<<<<< HEAD


# Notice to append an item to the list we used append method of the object
# There was no assignment, e.g. list2 = list2.append(6)
# There is no return value from the append method, so list2 would be empty []
=======
print(list2)
>>>>>>> 25ab74574c32a8647d987eaf88bf84ebc9e2579e
