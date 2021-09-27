class Shape:
    __height = 0
    __width = 0

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def area(self):
        pass

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width


class Triangle(Shape):
    def __init__(self, height, width):
        super().__init__(height, width)

    def area(self):
        return 1 / 2 * (self.get_height() * self.get_width())


class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__(height, width)

    def area(self):
        return self.get_height() * self.get_width()


rectangle = Rectangle(12, 9)
triangle = Triangle(12, 9)
print(rectangle.area())
print(triangle.area())
