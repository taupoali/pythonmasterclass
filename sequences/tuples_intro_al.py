<<<<<<< HEAD
t1 = "a", "b", "c"
print(t1)
print(type(t1))

name = "Al"
age = 50

t2 = ("Al", 50)
print(type(t2))

print(t2)

=======
t = "a", "b", "c"
print(t)
# the output is within parenthesis rather than square brackets as lists used
# we could have defined t as t=("a","b',"c")

name = "Ali"
age = "48"

print(name, age, "Python", 2020)
print((name, age, "Python", 2020))


# here are some tuples each with 3 items

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
# tuples are a sequence type so we can use indexing
print(metallica[0])
print(metallica[1])
# indexing works the same as with lists

# tuples are immutable
# metallica[0] = "Master of Puppets"

# tuples dont support all the methods needed for mutability
# so tuples use less memory than lists
# another adv is protecting integrity of your data

metallica2 = list(metallica)
print(metallica2)
>>>>>>> 25ab74574c32a8647d987eaf88bf84ebc9e2579e
