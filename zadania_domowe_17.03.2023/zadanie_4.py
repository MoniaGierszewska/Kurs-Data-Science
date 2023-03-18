# Napisać program, gdzie użytkownik podaje liczby całkowite i je sumuje.
# Program działa dopóki użytkownik nie poda liczby ujemnej.
# Po podaniu liczby ujemnej program wyświetla sumę podanych poprzednich liczb.

print("Program sumuje podane liczby całkowite. Koniec programu następuje po podaniu liczy ujemnej.")

suma = 0

while True:
    my_numbers = int(input("Podaj liczbę całkowitą: "))
    if my_numbers < 0:
        print(suma)
        break
    suma += my_numbers

