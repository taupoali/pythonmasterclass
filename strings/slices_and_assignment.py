# For mutable sequence types - 	# s[i] =x
# item i of s is replaced by x

# del s[i:j]


cars = ["Audi RS6", "Audi RS7", "BMW M5", "Mercedes C63"]
print(cars)
cars[1] = "Audi R8"
print(cars)


# For mutable sequence types - 	# s[i:j] = t
# slice of s from i to j is replaced by the contents of the iterable t

#cars[1:] = "Tesla Model X"


# del cars[3:]
print(cars)

del cars[2:]
print(cars)