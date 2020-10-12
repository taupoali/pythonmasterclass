# parrot = "Norwegian Blue"
# letter = input("Enter a character: ")
#
# if letter in parrot:
#     print("Letter {} is in {}".format(letter, parrot))
# else:
#     print("I dont need this letter")


activity = input("What do you want to do today? ")

# As regular string comparison would fail if i entered Cinema with capital C
# we can use casefold to get to lowercase - this is aggressive, e.g. German B would go to ss in this function

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")
