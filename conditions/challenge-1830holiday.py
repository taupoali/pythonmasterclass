name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if (name != "") and (18 <= age <= 30):
    print("Welcome {} to your holiday registration".format(name))
else:
    print("Sorry {}, but you have supply a name AND be between 18 and 30 to go on this holiday".format(name))
