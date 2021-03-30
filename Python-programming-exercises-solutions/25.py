from dataclasses import dataclass

@dataclass
class Person:
    name = 'Person'
    name : str

jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))

