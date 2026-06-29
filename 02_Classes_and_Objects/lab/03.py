class Circle:
    def __init__(self, radius, pi=3.14):
        self.radius = radius
        self.pi = pi

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_circumference(self):
        result = self.pi * self.radius * 2
        return result
    def get_area(self):
        result = self.pi * (self.radius) ** 2
        return result
    def calculate_area_of_sector(self, angle):
        result = (angle / 360) * self.pi * (self.radius) ** 2
        return result


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
