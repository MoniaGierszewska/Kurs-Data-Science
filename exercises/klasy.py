class Rectangle_area:
    def __init__(self):
     print("Prostokąt utworzony")


    def czytaj_dane (self, a,b):
        self.a = int(input("Podaj bok a: ")
        self.b = int(input("Podaj bok b: ")


    def przetworz_dane (self, a, b):
        self.pole = self.a * self.b
        return self.pole

    def wyswietla_wynik (self):
        print("Pole wynosi", self.pole, ".")


class Triangle_area(Rectangle_area):
    def __init__(self):
        super().__init__()