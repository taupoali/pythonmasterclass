name = "Al"
age = 48

print(name, age, "Python", 2020)
print(name, age, "Python", 2020, sep=", ")

# Now that we've supplied separator with sep= where the separator we've chosen is comma and space
# the parameters of the print function are now printed with that separator rather than the default separator

# sep can only be used when we pass more than 1 parameter to print otherwise it is ignored
