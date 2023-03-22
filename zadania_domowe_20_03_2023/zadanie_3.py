# ## Zadanie 03
# Napisz program, który narysuje trójkąt zależnie od podanego n
# Np. n = 3 to wynik jest
# ```
# *
# **
# ***
# ```
# Dodaj dekorator, który dodatkowo dopisze "-----------" na dole trójkąta oraz policzy liczbę *


def line_decorator(func):
    def star_count(l):
        suma = 0
        for i in range(1, l + 1, 1):
            suma += i
        return suma

    def wrapper(*args, **kwargs):
        k = args[0]
        print("`"*k)
        func(*args)
        print("`"*k)
        print(star_count(k))
    return wrapper

@line_decorator
def triangle (n):
    for i in range(1, n+1, 1):
        print(i * "*")

ile= int(input("Podaj ile gwiazdek ma być w trójkącie: "))
triangle(n=ile)


# # Dekorator dla funkcji, która przyjmuje argumenty oraz coś zwraca
# def trigger_info_return(func):
#     def wrapper(*args, **kwargs):
#         print(f"Wywołano funkcję {func}")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def star_count(n):
#     suma = 0
#     for i in range(1, n + 1, 1):
#         suma += i
#         return suma
#
#
# print(star_count(10))