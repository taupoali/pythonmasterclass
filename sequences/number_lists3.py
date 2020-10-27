empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# this is not concatentation
# this creates a list of lists!
numbers = [even, odd]
print(numbers)

# Here we use a nested for loop to iterate over nested lists
for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)