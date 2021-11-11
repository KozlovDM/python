import math


class Vector:
    def __init__(self, *args):
        if len(args) > 1:
            self.x = args[0]
            self.y = args[1]
        else:
            s = args[0].split(',')
            self.x = s[0]
            self.y = s[1]

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)


print('Первая задача\nВведите n')
n = int(input())
print('Введите %s точек' % n)
max_vector = Vector(0, 0)
all_abs_vectors = 0
for i in range(n):
    dot = input().split(',')
    vector = Vector(int(dot[0]), int(dot[1]))
    abs_vector = abs(vector)
    all_abs_vectors += abs_vector
    if abs_vector > abs(max_vector):
        max_vector = vector
print('Самая удаленая точка ' + str(max_vector))
print('Самая удаленая точка ' + str(all_abs_vectors / n))
