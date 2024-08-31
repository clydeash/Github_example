# Python Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

person1 = Person("Clyde", 8)

print(person1.name)
print(person1.age)
person1.greet()