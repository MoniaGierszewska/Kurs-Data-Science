## Zadanie 02
#
# Napisz moduł, który będzie posiadał funkcje obliczające:
#
# * Funkcje kwadratową (zwraca listę rozwiązań)
# * Pierwiastek drugiego stopnia z podanej liczby
# * N element ciągu harmonicznego (prośba o weryfikacje czym jest ciag z netem)

def my_quadratic(a):
    return a ** 2


def my_square(a):
    return a ** 1/2


def my_harmonic(n):
    for i in range(1, n+1):
        print("1 /", i)
        i+=1


print(my_quadratic(5))

print(my_square(4))

my_harmonic(2)