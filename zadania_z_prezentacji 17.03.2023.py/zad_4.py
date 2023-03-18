# Stwórz funkcję, która sprawdzi, czy podany jako argument napis jest  palindromem
# (tj. czytany od przodu i wspak jest dokładnie taki sam, np. „kajak”, „Madam”).

def is_palindrom (txt):
    if txt == txt[::-1]:
        print("Palindrom!")
    else:
        print("Niestety nie!")

is_palindrom ("kajak")