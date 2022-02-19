"""
Liscov Substitution principle
"""


class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    def __str__(self):
        return f"Width: {self.width}, Height: {self.height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @width.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10  # Breaks LSP
    expected = int(w * 10)
    print(f"Expected area: {expected}, got: {rc.area}")


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)