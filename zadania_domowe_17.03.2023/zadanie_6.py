# Zadanie 06
# Użytkownik podaje liczbe całkowitą. Następnie program zwraca sumę CYFR z których składa się podana liczba.
# Przykładowo: użytkownik podaje 1307, program zwraca 11 (1+3+0+7). Podpowiedź: konwersja na str

my_num = int(input("Podaj liczbę całkowitą:"))
converted_num = str(my_num)

suma = 0

for n in converted_num:
    m = int(n)
    suma += m
print(suma)