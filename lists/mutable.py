# this is the one that will catch you out!
# think of the name of the list as a pointer to the data and you can have many pointers to same data
# correct terminology is name BOUND to an OBJECT
# in this case there is only 1 OBJECT - the list OBJECT
# THE LIST OBJECT IS MUTABLE

shopping_list = ["Bread", "Milk", "Cheese"]
print(shopping_list)
another_list = shopping_list
print(another_list)

print("\nFirst we show the id of shopping_list")
print(id(shopping_list))
print("Now we show the id of another_list which was set to equal shopping_list")
print(id(another_list))

print("\n\nNow append method to the list so biscuits is added")
shopping_list.append("Biscuits")

print(id(shopping_list))
print(id(another_list))

print(shopping_list)
print(another_list)

a = b = c = another_list
print(id(a))
print(id(b))
print(id(c))
