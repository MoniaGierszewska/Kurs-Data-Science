class Employee:
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.__age = age


    #getter
    @property
    def age(self):
        return self.__age

    #Setter
    @age.setter
    def age(self, new_age):
        self.__age = new_age

p1 = Employee("Jan", "Kowalski", 30)
print(p1.age)
p1.f_name = "Adam"
print(p1.f_name)