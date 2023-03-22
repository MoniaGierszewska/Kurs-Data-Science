class Student:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.grades = []
        self.avg_grade = 0.0

    def add_grade(self, grade):
        if grade in (2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0):
            self.grades.append(grade)
            self.avg_grade = sum(self.grades) / len(self.grades)
            print ("Dodano ocenę")
        else:
            print("Ocena nieprawidłowa")

    def __str__ (self):
        return f"{self.imie} {self.nazwisko},- {self.avg_grade}"

    def __int__(self):
        return int(sum(self.grades))

    def __float__(self):
        return float(self.avg_grade)


s1 = Student("Karolina","Kowalska")
print(s1.imie, s1.grades)

s1.add_grade(5.0)
s1.add_grade(4.0)
s1.add_grade(4.0)
print(s1.avg_grade)
print(float(s1))