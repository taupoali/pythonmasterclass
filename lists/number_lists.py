even = [2, 4, 6, 8]
print("The ID of the even list is {}".format(id(even)))
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()
print(len(even))
print(len(odd))

print()
print("mississippi".count("ss"))

# takes all the items in the iterable and adds them to the list
# but note the resulting list is not in order
even.extend(odd)
print(even)
print("The ID of the even list is {}".format(id(even)))
# Now using the sort method
even.sort()
print(even)

# The items are reordered WITHOUT creating a copy of the data
# We are changing the contents of the same list
# Remember lists are a MUTABLE data type
# Imagine your list is serveral GB in size

print("The ID of the even list is {}".format(id(even)))
even.sort(reverse=True)
print(even)

another_even = even
print(another_even)
print("The ID of the even list is {}".format(id(another_even)))