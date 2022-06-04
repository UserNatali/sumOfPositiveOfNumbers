class Circle:
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius

    def get_perimetr(self):
        return 2 * self.PI * self.radius

    def get_area(self):
        return 2 * self.PI * self.radius ** 2

c = Circle(3)
print(c.get_perimetr())
print(c.get_area())