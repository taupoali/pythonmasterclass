#         01234567890123
parrot = "Norwegian Blue"
print(parrot)
print(parrot[-11])
print(parrot[-10]+ "\n" +" \n"  + parrot[-11] + "\n" + parrot[-8] + "\n" + parrot[-6] )
# watch for negative indexing starting at 1

# first number start at second number stop at
# slice up to but not including index position 6
print(parrot[0:6])

# up to but not including is also found in Python ranges

print(parrot[3:5])
print(parrot[0:9])

# if we omit start at then we still need the colon
print(parrot[:9])

print(parrot[10:14])
# we can omit the end value also
print(parrot[10:])
# could we omit both numbers?
print(parrot[:])

# negative indices count from right side
# can use 2 negatives to reference start and up to but not including
# can use 1 negative and a positive, just means where you count from is different

print("\nNow do negatives\n")
#           01234567890123
# parrot = "Norwegian Blue"
print(parrot[-4:])
print(parrot[-4:-3])
print(parrot[-4:-2])
print(parrot[-6:])
print(parrot[-6:12])
print(parrot[-9:])
print(parrot[-9:9])

print(parrot[1:-4])
print("###### Now steps")
print(parrot[0:10:2])
print(parrot[1::3])
print(parrot[-4:-14:-2])
print(parrot[-14:-1:2])
