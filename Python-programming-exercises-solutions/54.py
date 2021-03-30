from dataclasses import dataclass
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

@dataclass
class Square(Shape):
    length : float
    def area(self):
        return self.length**2

aSquare= Square(3)
print(aSquare.area())