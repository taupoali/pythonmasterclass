import math

x = 25
print(x)
print(id(x))
y = x
print(y)
print(id(y))

print("the ids are the same - pointing at same object")

// because we are assigning with = its different from list1.append(8)
// as list is the object and append the method on that class

print("increase x")
x += 100
print("the val of x is", x)
print("y val is still ", y)


print("the ids of x and y are")
print(id(x))
print(id(y))

print("so its the new value assigned to x that creates a new id")