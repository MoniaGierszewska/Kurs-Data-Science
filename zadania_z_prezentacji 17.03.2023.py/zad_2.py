# Stwórz funkcję przyjmującą listę liczb całkowitych, a zwracającą informację,
# na której pozycji znajduje się najmniejsza liczba.
# Nie korzystaj z wbudowanych funkcji.
# np. dla listy [42, 13, 56, 7, 12, 3, 85] funkcja powinna zwrócić 5,
# ponieważ pod tym indeksem w tej liście znajduje się element najmniejszy.

my_list = [42, 13, 56, 7, 12, 3, 85, 13, 12, -5]

def checking_min_list (liczby):
    najmniejsza = liczby[0]
    indeks = 0
    for n in range(0,len(liczby)):
        if liczby[n] < najmniejsza:
            najmniejsza = liczby[n]
            indeks = n
    return indeks

print(checking_min_list(my_list))
