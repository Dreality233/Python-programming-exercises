from math import pi
from dataclasses import dataclass

@dataclass
class Circle():
    radius : float

    def area(self):
        return self.radius**2*pi

aCircle = Circle(2)
print(aCircle.area())