shopping_list = ["Milk", "Pasta", "Eggs", "Spam", "Bread", "Rice"]

item_to_find = input("What item are you looking for? ")
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

print("Your item {} was found at position {}".format(item_to_find, found_at))
