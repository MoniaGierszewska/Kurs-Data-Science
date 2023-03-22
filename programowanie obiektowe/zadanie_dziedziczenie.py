class Person:
    def __init__(self, name, surname, adres, age):
        self.name = name
        self.surname = surname
        self.adres = adres
        self.age = age

    def __str__(self):
        return f"{self.surname}, {self.name}, {self.adres}"

    def check_is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


class Customer (Person):
    def __init__(self, name, surname, adres, age, orders, login, total_order_cost):
        super().__init__(name, surname, adres, age)
        self.orders = []
        self.login = login
        self.total_order_cost= total_order_cost

    def __str__(self):
        return f"{self.login} - {super().__str__()}"

    def add_order(self, product, cost):
        # if self.age >= 18:
        if super().check_is_adult():
            self.orders.append((product, cost))
            self.total_order_cost += cost
        else:
            print("Osoba nie jest pełnoletnia")

    def show_orders(self):
        for n in self.orders:
            print (n)

p1 = Customer("Monika", "Gierszewska", "Słowackiego 11", 19, ("Karta", 10), "moni", 5 )
print(p1.check_is_adult(), p1.surname)
print(p1)

add_order(("credit", 1000000))