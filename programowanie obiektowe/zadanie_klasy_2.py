class Animal:
    def __init__(self, legs_count, eyes_count, name, weight):
        self.legs_count = legs_count
        self.eyes_count = eyes_count
        self.name = name
        self.is_alive = True
        self.weight = weight

    def __str__(self):
        return self.name

    def running(self):
        print("Tup tup tup tup tup")

# a1 = (4, 2, "mouse")
# a2 = (2, 2, "bird")

# print(a1.name)

class Dog(Animal):
    def __init__(self, legs_count, eyes_count, name, weight, race):
        super().__init__(legs_count, eyes_count, name, race)
        self.race = race

    def __str__(self):
        return f"{super().__str__()} - {self.race}"


d1 = Dog(4,2,"Burek", 30, "Husky")
print(d1.is_alive, d1.race)
print(d1)

d1.running()