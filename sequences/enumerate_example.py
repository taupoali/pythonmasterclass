for index, character in enumerate("abcdefgh"):  # This is very efficient
    print(index, character)                     # Remember all sequences are iterable

# the above is really shorthand for the below
# enumerate gives us a tuple for each iteration
# so in the code below we are unpacking tuple t to variables index and character

for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)