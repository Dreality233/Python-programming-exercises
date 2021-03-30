from dataclasses import dataclass
@dataclass
class Rectangle():
    length : float
    width : float

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print(aRectangle.area())