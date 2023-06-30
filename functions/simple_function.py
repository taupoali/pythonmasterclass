# the def keyword is used to define a function
# here we know the number of arguments
def sumnums(a, b):
    return a + b


print(sumnums(4, 3))

# lets define 2 lists
mylist1 = [2, 6, 10]
mylist2 = [99, 101, 244]

# now we are calling the same function but the args are lists not scalers and it still works
print(sumnums(mylist1, mylist2))

mytuple1 = ("Metallica", "Master of Puppets")
mytuple2 = ("Iron Maiden", "Powerslave")
print(id(mytuple1))
print(id(mytuple2))

# this works as we are not mutating the tuples
print(sumnums(mytuple1, mytuple2))

mytuple1 = mytuple1 + mytuple2
print(mytuple1)
print(id(mytuple1))

x = lambda a: a + 10
print(x(5))
