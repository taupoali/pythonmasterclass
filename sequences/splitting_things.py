panagram = """The quick brown
fox jumps\tover
the lazy dog"""

# words = panagram.split()
# print(words)

# defaults to splitting on space

# Now lets split a string using a separator of comma
# this will create a list of strings - they are not ints

my_numbers = "9,223,372,036,654,775,807"
generated_nums = my_numbers.split(",")
print(generated_nums)

for index in range(len(generated_nums)):
    newnum = int(generated_nums[index])
    generated_nums[index] = newnum

print(generated_nums)
# constructed = " ".join(generated_nums)
# print(constructed)

