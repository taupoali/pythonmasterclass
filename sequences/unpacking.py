a = b = c = d = e = f = 42
print("we are setting a = b = c = d = e = f = 42")
print("the value of c is", c)

# unpacking a tuple
print("we are setting x, y, z = 1, 2, 76")
x, y, z = 1, 2, 76

print(x)
print(y)
print(z)

print("Unpacking a tuple")
data = 1, 2, 76  # data represents a tuple
print("we set data = 1, 2, 76")
print("the type of data is ", type(data))
print("we do the unpack by assignment of new vars x, y, z = data")
x, y, z = data
print(x)
print(y)
print(z)

# tuples can't be on the left of the assignment as they are immutable
# because a tuple can't be changed you can ALWAYS unpack a tuple
# you can ALWAYS unpack a tuple because its immutable so you KNOW how many items are in it

print("Unpacking a list")
print("we are setting data_list = [12, 13, 14]")
data_list = [12, 13, 14]
print(data_list)
print(type(data_list))
print("now we are using the append method on list class object data_list")
data_list.append(15)
print(data_list)

p, q, r = data_list  # we are trying to unpack a tuple with 4 items into 3 vars - ValueError: too many values to unpack
print(p)
print(q)
print(r)
#print(s)
p, q, r  = data_list
print(p)
print(q)
print(r)
print(s)
# we can unpack any sequence type
# unpacking a list is possible, but lists are mutable
# so if we append to the list, it breaks the code
# we don't know how many items will be in it as (like above) you can append to lists

