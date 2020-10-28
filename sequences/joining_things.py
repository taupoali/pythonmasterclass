flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]

for flower in flowers:
    print(flower)

print("\n\n")

separator = " | "
output = separator.join(flowers)
print(output)

# Each of the flowers has been joined to a single string with | as separator
# we didn't need a for loop, instead join iterates over the list for you!!
# we were very verbose here so the code is clear to understand, but we could do more on 1 line like

print(", ".join(flowers))

# all the items in the iterable must be strings for this to work, we can't join ints to strings etc
