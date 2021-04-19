# Example 1: Create class method using classmethod()

class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

# create printAge class method
Person.printAge = classmethod(Person.printAge)

Person.printAge()

# Output

# The age is: 25


# Example 2: Create factory method using class method

from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display() 

person1 = Person.fromBirthYear('John',  1985)
person1.display()


# Output

# Adam's age is: 19
# John's age is: 31


# Example 3: How the class method works for the inheritance?

from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'

man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))

# Output

# True
# False
