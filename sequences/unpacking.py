a = b = c = d = e = f = 42
print(c)

# unpacking a tuple
x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a tuple")
data = 1, 2, 76 # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)
# tuples cant be on the left of the assignment as they are immutable
# because a tuple can't be changed you can ALWAYS unpack a tuple
# you can ALWAYS unpack a tuple because its immutable so you KNOW how many items are in it

print("Unpacking a list")
data_list = [12, 13, 14]
data_list.append(15)
p, q, r  = data_list
print(p)
print(q)
print(r)
print(s)
# we can unpack any sequence type
# unpacking a list is possible, but lists are mutable
# so if we append to the list, it breaks the code
# we don't know how many items will be in it as (like above) you can append to lists

