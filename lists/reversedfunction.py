data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# 13 values in the list
# index positions 0 to 12 forward, or 12 to 0 backwards
# remember lists are SEQUENCES
# U

top_index = len(data) - 1

for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

# enumerate is efficient particularly above 1000 items



