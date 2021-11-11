import math


class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return str(self.real) + ('+' if self.imag >= 0 else '') + str(self.imag) + 'j'

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.imag)

    def __truediv__(self, other):
        return Complex((self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2),
                       (self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2))

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)


def my_print(text, complex1, complex2):
    print(text)
    print(complex1)
    print(complex2)
    print(complex1 + complex2)
    print(complex1 - complex2)
    print(complex1 * complex2)
    print(complex1 / complex2)
    print(abs(complex1))


my_print("Мой класс", Complex(1, 2), Complex(3, 4))
my_print("\nВстроенный класс", complex(1, 2), complex(3, 4))
