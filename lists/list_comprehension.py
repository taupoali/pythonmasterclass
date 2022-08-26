my_list = [2,5,7,88]
print(my_list)
print(type(my_list))
print(len(my_list))

my_list2 = [str(i) for i in range(1,len(my_list))]
print(my_list2)

my_list3 = [i for i in my_list: ]