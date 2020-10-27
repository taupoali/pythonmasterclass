menu = [
        ["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
]
# redundant comma is deliberate
# makes easier to copy and paste and still have desired effect when you reorder

for meal in menu:
        if "spam" not in meal:
                print(meal)

                for item in meal:
                        print(item)
        else:
                print("{0} has a spam score of {1}".format(meal, meal.count("spam")))

