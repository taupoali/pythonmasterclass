# In this range, we start at 1 (not zero) and up to but not including 20
for i in range(1,20):
    print("i is now {}".format(i))

# Now if we exclude starting value, it defaults to zero
# So here, its zero up to but not including 10
for i in range(10):
    print(i)

# Now if we include a step size
for i in range(0, 10, 2):
    print(i)

print("*" *80)

# We can also use a negative step
# This would be 10 down to 1 remembering upto/downto but NOT including stop value
for i in range(10, 0, -1):
    print(i)