data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# 13 values in the list
# index positions 0 to 12 forward, or 12 to 0 backwards

# range(start, stop, step) which would be here range(12, -1, -1)

for index in range(len(data) - 1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        print(index, data)
        del data[index]

print(data)
