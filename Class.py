class Person:
    def print_info(self):
        print(f"Name:{self.name}, Surname:{self.surname}, Place_of_birth:{self.place_of_birth}")

    def get_age(self):
        from datetime import date
        todays_date = date.today()
        current_year = todays_date.year

        return current_year - self.year_of_birth


human1 = Person()
human1.name = "Elon"
human1.surname  = "Mask"
human1.place_of_birth = "ЮАР"
human1.year_of_birth = 1970

human2 = Person()
human2.name = "Natalia"
human2.surname = "Koval"
human2.place_of_birth = "Kyiv"
human2.year_of_birth = 1978

print(f"Name:{human1.name}, Surname: {human1.surname}, Place_of_birth:{human1.place_of_birth}")
print(f"Name:{human2.name}, Surname: {human2.surname}, Place_of_birth:{human2.place_of_birth}")

human1.print_info()
human2.print_info()


print(human1.get_age())
print(human2.get_age())