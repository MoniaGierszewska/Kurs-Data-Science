class Product:
    def __init__(self, name, category, sn, price):
        self.name = name
        self.category = category
        self.__sn = sn
        self.__price = price

    @property
    def sn(self):
        return self.__sn


    @sn.setter
    def sn(self, new_sn):
         self.__sn = new_sn


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price):
        if new_price < 0.01:
            self.__price = 0.01
        else:
            self.__price = new_price


p1 = Product("Intel i7", "CPU", "000-000-0001", 4999.99)
p1.price = 5200

print(p1.name, p1.price)

