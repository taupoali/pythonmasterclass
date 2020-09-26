from typing import List

user_input = None
user_options: List[str] = ["Learn Python", "Learn Java", "Learn NodeJS", "Learn BASIC"]


def show_list():
    for i in range(0, len(user_options)):
        print("{}) {}".format(i+1, user_options[i]))


print("Make your selection, 0 to quit")
show_list()
while user_input != "0":
    user_input = input(">")
    if int(user_input) > len(user_options):
        show_list()
    elif user_input == "0":
        pass
    else:
        print("Good choice to {}".format(user_options[(int(user_input)-1)]))
else:
    print("Thanks for playing!")