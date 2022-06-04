class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person created")

    def say_hello(self):
        print(f"{self.name} says hello!")

class Student(Person):
    def __init__(self, name, age, everage_grade):
        super().__init__(name, age)
        self.everage_grade = everage_grade
        print("Student created")

    def study(self):
        print(f"{self.name} studies")

    def say_hello(self):
        super().say_hello()
        print(f"Student with name {self.name} says hello!")

class Teacher(Person):
    def teach(self):
        print(f"{self.name} teaches")

def introduce(person):
    print("Hello")
    person.say_hello()

people = [Student("Tom", 18, 3.5),Teacher("Elen", 32)]
for el in people:
    introduce(el)


