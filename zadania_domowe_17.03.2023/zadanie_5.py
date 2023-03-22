# Zadanie 05
# Napisać funkcję, która konwertuje liczbę z systemu dziesiętnego na binarny
# (nie używamy funkcji wbudowanych w Pythonie)

5

def dec_to_bin(value: int):
    parts = []

    while value != 0:
        parts.append(value % 2)
        value //= 2

    return parts[::-1]

print(dec_to_bin(20))

#jest funkcja wbudowana bin która zwraca liczbę binarną