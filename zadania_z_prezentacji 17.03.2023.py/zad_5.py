# Stwórz funkcję, która obliczy liczbę małych i wielkich liter w ciągu.
# np. dla : “The quick Brown Fox”
# oczekiwany wynik :
# LIczba wielkich liter : 3, liczba małych liter : 13
# Podpowiedź: wykorzystaj pętlę, instrukcję warunkową i odpowiednie metody dla stringa.

def up_low_check (txt):
    up = 0
    low = 0
    for n in txt:
        if n.isupper():
            up += 1
        elif n.islower():
            low += 1
    print("Liczba wielkich liter : ", up, " liczba małych liter : ", low)

up_low_check("The      quick  Brown   Fox")