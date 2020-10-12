shopping_list = ["Bread", "Oatley Milk", "Brown Rice", "Spam"]
print(shopping_list)

#print(shopping_list[0])
# Using continue meant we skip the remaining instructions in this iteration of the loop, so the print buy spam is
# skipped. Any code that was indented belonging to the same code block would have been skipped
for item in shopping_list:
    if item == "Spam":
        continue
    print("Buy {}".format(item))

new_list = shopping_list

print(new_list)
new_list.append("Coco pops")
print(new_list)

# Now the crazy part, this gives same output as new_list
# When copying a list, you get 2 variable names (like pointers) to the same memory
# so modifying the value of new_list meant we were upating the memory area where shopping_list pointed to
print(shopping_list)


# Sets are unordered, you can't reference an index position like [2] as there is no index
# You can add to a set with .add()
# Same thing with sets, modify 1 and any copies are modified too as the variable name of copy is just a pointer
newset = {"apple", "banana", "cherry"}
print(newset)
newset2 = newset
print(newset2)
newset2.add("grapes")
print(newset2)
print(newset)
