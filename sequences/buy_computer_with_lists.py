available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive",
                   "gpu"]
valid_choices = [str(i) for i in range(1, len(available_parts) +1)]    # comprehension
print(valid_choices)
current_choice = "-"
computer_parts = [] # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) -1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # its already in the list so remove
            print("Removing item from your cart")
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        for number, part in enumerate(available_parts):   #powerful, we get index position and item as pair in the loop
            print("{0}: {1}".format(number +1, part))

    current_choice = input()

print(computer_parts)