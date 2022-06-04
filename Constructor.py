class Person:
    numerosity = 123
    number = 0
    def __init__(self, name, surname, place_of_birth, year_of_birth):
        self.name = name
        self.surname = surname
        self.place_of_birth = place_of_birth
        self.year_of_birth = year_of_birth
        Person.number += 1


    def print_info(self, n):
        for i in range(n):
            string1 = f"Name:{self.name}, " \
                  f"Surname:{self.surname}," \
                  f" Place_of_birth:{self.place_of_birth}, " \
                  f"Year_of_birth:{self.year_of_birth} "
            print(string1)

human1 = Person("Elon", "Mask", "ЮАР", 1970)
human2 = Person("Natalia", "Koval", "Kyiv", 1978)
human3 = Person("Albert", "Einstein", "Германия", 1879)
human1.print_info(1)
human2.print_info(1)
human3.print_info(1)
print(human1.name)
human1.numerosity  = 789

print(human2.numerosity)
print(human1.number)


