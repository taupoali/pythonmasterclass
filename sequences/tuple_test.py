# This isnt like ordinary assignment of value to variables
# You have two variable names pointing at same memory!
# In this example we are using tuples, which are immutable
# So changing one and checking the other makes no sense
# But in the following code you can see that tup2 is essentially tup1, they have the same id
tup1 = (1,2,3,4,5)
print(tup1)
tup2 = tup1
print(tup2)
print(id(tup1))
print(id(tup2))
