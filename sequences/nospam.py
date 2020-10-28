menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# print out all the meals in the menu but with spam removed
# produce 8 meals all without spam

# This 1st method just prints out the menu meals without spam listed, the lists themselves are unmodified
# Notice we are using end in the print function, the default is a newline, but here we are using space
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=" ")
    print()


# This 2nd method uses reverse mutation of the sequence we are iterating over
# so we are removing items from the meal lists
for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

print(menu)

