class Animal:
    __name = None
    __age = None

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return self.__name + " " + str(self.__age)


class Zebra(Animal):
    def __str__(self):
        return super().__str__() + " " + "Zebra"


class Dolphin(Animal):
    def __str__(self):
        return super().__str__() + " " + "Dolphin"


zebra = Zebra("зебра", 2)
print(zebra.__str__())
zebra = Dolphin("дельфин", 2)
print(zebra.__str__())
