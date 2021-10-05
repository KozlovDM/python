class Shape:
    _height = None
    _width = None

    def __init__(self, height, width):
        self._height = height
        self._width = width

    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, height, width):
        super().__init__(height, width)

    def area(self):
        return 1 / 2 * (self._height * self._width)


class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__(height, width)

    def area(self):
        return self._height * self._width


rectangle = Rectangle(12, 9)
triangle = Triangle(12, 9)
print(rectangle.area())
print(triangle.area())
