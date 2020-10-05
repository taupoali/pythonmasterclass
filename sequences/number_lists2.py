print("Lets think about how we create **new** lists\n")
empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print("here is the even list: {} with id of {}".format(even, id(even)))
print("here is the odd list {} with id of {}".format(odd, id(odd)))

print("\nNow lets create a new list with numbers = even + odd")
numbers = even + odd
print("Here's the new list: {} with id {}".format(numbers, id(numbers)))

print("\nLets now create a new list sorted_numbers = sorted(numbers")
sorted_numbers = sorted(numbers)
print("here is the sorted_numbers: {} with id of {}".format(sorted_numbers, id(sorted_numbers)))

print("\nNow lets create a new list with digits = sorted('432985617')")
digits = sorted("432985617")
print(digits)
print("this is a list of strings")

print("\nNow lets look at list class which we are using here as if just a function")
print("the numbers list variable has value")
print(numbers)
print("Now lets create more_numbers by using = list(numbers)")
more_numbers = list(numbers)
print(more_numbers)
print("These are not the same tho i.e. different Ids- lets check:")
print(numbers is more_numbers)
print("Lets print the ids of numbers and more_numbers to confirm they are indeed different")
print(id(numbers))
print(id(more_numbers))
print("Interestingly if we check the lists are equal with == we get")
print(numbers == more_numbers)
print("This is because the == operation is checking the values of the items")


# we could also use slices to create new lists, just as we did with strings

more_numbers2 = numbers.copy()
print(more_numbers2)
print(id(more_numbers2))
