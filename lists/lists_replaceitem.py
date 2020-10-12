computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"]

print(computer_parts)
# Now we will replace item at index 3 - the 4th item in the list as we start index at zero
# Order of items will be maintained
# Lists are MUTABLE
# computer_parts[3] = "trackball"
# print(computer_parts)

print(computer_parts[3:])
computer_parts[3:] = ["trackball"]
print(computer_parts)

# We used slicing in both examples [3:] to say from item at index 3 to end of list 
# We had to make the right side a list, as trackball was a string, which is iterable
# So until we made it a list by wrapping in [] we got each char added to list