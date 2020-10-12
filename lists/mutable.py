# this is the one that will catch you out!
# think of the name of the list as a pointer to the data and you can have many pointers to same data
# correct terminology is name BOUND to an OBJECT
# in this case there is only 1 OBJECT - the list OBJECT
# THE LIST OBJECT IS MUTABLE

shopping_list = ["Bread", "Milk", "Cheese"]

another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

shopping_list.append("Biscuits")

print(id(shopping_list))
print(id(another_list))

print(shopping_list)
print(another_list)

a = b = c = another_list
print(id(a))
print(id(b))
print(id(c))
