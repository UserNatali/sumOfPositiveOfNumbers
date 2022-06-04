class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"Dog {self.breed} named {self.name} is barking")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says meow")

class Frog(Animal):
    def eat(self):
        print(f"Frog with {self.name} is eating")

dog = Dog("Rex","shepherd")
cat = Cat("Mur")
frog = Frog("Busia")
dog.bark()
dog.eat()
cat.meow()
cat.eat()
frog.eat()
frog.eat()
print(dog.breed)


