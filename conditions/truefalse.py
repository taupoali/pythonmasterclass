day = "Monday"
temperature = 30
raining = True

if day == "Saturday" and temperature > 27 and not raining:
    print("Go Swimming")
else:
    print("Learn Python!")

# Think about intent
# Think about operator precedence
# By using parenthesis we can clearly read that the day and temp conditions must be evaluated first as AND
# The outcome of that AND expression is then OR'd with the expression not raining

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go Swimming")
else:
    print("Learn Python!")

# Let's now consider truthy values
# Things like zero or empty strings are evaluated as false
# If you hit enter on the input prompt below, name is empty, therefore evaluates to false and else code runs

name = input("What's yer name? ")
if name:
    print("Alright {}".format(name))
else:
    print("Shy are are we?")

# However think intent and readability
# So if name != "" would be clearer to read and understand

