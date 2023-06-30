
t1 = "a", "b", "c"
print(t1)
print(type(t1))
print("")

name = "Al"
age = 50

t2 = (name, age)
print(t2)
print(type(t2))
print("")

t = "a", "b", "c"
print(t)
print(type(t))
print("")
# the output is within parenthesis rather than square brackets as lists used
# we could have defined t as t=("a","b',"c")

name = "Ali"
age = "48"

print(name, age, "Python", 2020)
print((name, age, "Python", 2020))
print("")

# here are some tuples each with 3 items

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(welcome)
print(type(welcome))
print("")
print(metallica)
# tuples are a sequence type so we can use indexing
print(metallica[0])
print(metallica[1])
# indexing works the same as with lists

# tuples are immutable
#metallica[0] = "Master of Puppets"

# tuples dont support all the methods needed for mutability
# so tuples use less memory than lists
# another adv is protecting integrity of your data

metallica2 = list(metallica)
print(metallica2)
print(type(metallica2))
