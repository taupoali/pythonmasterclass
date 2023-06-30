# This isnt like ordinary assignment of value to variables
# You have two variable names pointing at same memory!
# In this example we are using tuples, which are immutable
# So changing one and checking the other makes no sense
# But in the following code you can see that tup2 is essentially tup1, they have the same id

print("this is tup1")
tup1 = (1,2,3,4,5)
print(tup1)

print("now we are assigning tup2 = tup1")
tup2 = tup1
print("here is tup2")
print(tup2)
print("\nHere is the ids of both")
print(id(tup1))
print(id(tup2))
print("\n\n")

# tuples are immutable, so no append method, but we can emulate with concatenation
# but we end up with a new object

a_tuple = (1,2,3)
b_tuple = (4,5,6)

print(a_tuple)
print(b_tuple)
print(id(a_tuple))
print(id(b_tuple))

a_tuple = a_tuple + b_tuple
print(a_tuple)
print(id(a_tuple))

print("we ended up with 3 unique tuples with unique ids")
