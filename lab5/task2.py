class Mother:
    def __str__(self):
        return "Mother"


class Daughter(Mother):
    def __str__(self):
        return "Daughter"


mother = Mother()
daughter = Daughter()
print(mother)
print(daughter)
