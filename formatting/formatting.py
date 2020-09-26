print("{2} days in Jan\n{0} days in Feb \n{1} days in March".format(29, 30, 31))
# With range its starting at and up to but not including

# for i in range(1000, 1010):
#     print("Loop counter is: {:5<}".format(i))

name = input("What is your name? ")
age = int(input("What is your age {}?".format(name)))
print("Next year you will be {1} {0}".format(name, age+1))

if age <18:
    print("Not yet, come back in {} years".format(18-age))
elif age == 900:
    print("Yoda, we meet again")
else:
    print("Proceed to vote!")

pi = 22/7
# print("Approx val of pi to 20 places is {:12.20f}".format(pi))
# print("Approx val of pi to 50 places is {:12.50f}".format(pi))

