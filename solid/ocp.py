"""
Open-Closed principle: Open for extension,  closed for modification.
"""
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):  # Breaks OCP
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, color, size):  # State space explosion
        for p in products:
            if p.size == size and p.color == color:
                yield p


# Specification -> Enterprise pattern

class Specification:
    def is_satisfied(self, item):
        ...

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        ...


class Filter:
    def filter(self, item, specification):
        ...


class ColorSpecification(Specification):

    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):

    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(
            map(lambda spec: spec.is_satisfied(item), self.args)
        )


class BetterFilter(Filter):
    def filter(self, items, specification):
        for item in items:
            if specification.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product("Apple", Color.RED, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.MEDIUM)
    car = Product("Car", Color.BLUE, Size.LARGE)

    products = [apple, tree, car]

    # Old approach
    pf = ProductFilter()
    print("Green products (old)")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f" - {p.name} is green")

    # New approach

    bf = BetterFilter()
    print("Green products (new)")
    green = ColorSpecification(Color.GREEN)

    for p in bf.filter(products, green):
        print(f" - {p.name} is green")

    print("Large products")

    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name} is large")

    large_blue = large & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is large and blue")
