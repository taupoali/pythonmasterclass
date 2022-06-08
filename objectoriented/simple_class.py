
class Person:
    def __init__(self, nameparammeter, addressparameter):
        self.name = nameparammeter
        self.address = addressparameter

    # The __str__ method in Python represents the class objects as a string
    # it can be used for classes.
    # The __str__ method should be defined in a way that is easy to read and outputs all the members of the class.
    # This method is also used as a debugging tool when the members of a class need to be checked.
    def __str__(self):
        return f"{self.name}, {self.address}"


def main() -> None:
    personobj = Person("Alistair", "26 St Ninians")
    print(personobj)


# We can use an if __name__ == "__main__" block to allow or prevent parts of code from being run when the modules 
# are imported. When the Python interpreter reads a file, the __name__ variable is set as __main__ if the module 
# being run, or as the module's name if it is imported.

if __name__ == "__main__":
    main()

