# Immutable data types in Python are
# Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
# Strings
# Tuples
# In this code we use numbers (boolean) and strings

print("Set a variable called result to boolean True")
result = True
another_result = result
print("Lets start by printing the ids of result and another_result")
print(id(result))
print(id(another_result))

# the id function returns the identity of an object

# in the statement below, we are creating a new OBJECT with a new id
# it will no longer be the same thing as the first
# the object is immutable
# what looks like assigning a new value, is in fact creating a new OBJECT

result = False
print("\n\nNow lets look at ids for the result and another_result variables after changing result")
print(id(result))
print(id(another_result))

print("\n\nLets look at ids for string1 and string2")
mystring1 = "Cheese"
mystring2 = mystring1
print(id(mystring1))
print(id(mystring2))
# now try and change an immutable object
mystring1 += "  ham"
print(mystring1)
print(mystring2)
print(id(mystring1))
print(id(mystring2))
