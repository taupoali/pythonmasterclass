# parrot = "Norwegian Blue"
#
# for character in parrot:
#     print(character)

number = "9,223;372:036 854,775;807"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
print(separators)
