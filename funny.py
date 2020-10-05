import random
x = random.randint(1,7)
#print(x)
your_name = input("What is your name? ")
if x == 1:
    print("Well {}, I think you have done a poo in your pants!".format(your_name))
elif x == 2:
    print("Well {}, I think you have done a pee on the floor!".format(your_name))
elif x == 3:
    print("Well {}, I think you have done a smelly fart!!".format(your_name))
elif x == 4:
    print("Well {}, I think you need a poo!".format(your_name))
elif x == 5:
    print("Well {}, I think you need a haircut!".format(your_name))
elif x == 6:
    print("Well {}, I think you have pee pee on your poo poo!".format(your_name))
else:
    print("Computer needs poo now.")


