pangram: str = "The quick brown fox jumps over the lazy dog"
print(id(pangram))

# Here we are using the built-in sorted function
# We are creating a new list with rearranged values

letters = sorted(pangram)
print(letters)
print(id(letters))


# Make sure you are cautious with variable names
# Don't use names of builtin functions as vars! Crazy that Python lets you do this...

numbers = [2.3, 4.5, 8.7, 9.2, 1.6]
print(numbers)
print(id(numbers))
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(id(sorted_numbers))

# Here we adding a string literal as param to sorted
missing_letter = sorted("The quick brown foxed jumped over the lazy dog", key=str.casefold)
print(missing_letter)

# This is different from .sort
# Which changes the list
# Sort method does not return a value


names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"]

# Be careful here not to have casefold() i.e. we don't want parenthesis
# We are not calling the function here, we are passing an argument to sort function which will in turn use that method
names.sort(key=str.casefold)
print(names)
