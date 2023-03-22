## Zadanie 01
#
# Napisz funkcję, która jak argument przyjmuje listę liczby całkowitych,
# a zwraca wartość int jako największa liczba z listy (nie wolno używać max).
#
# Dodatkowo zabezpiecz program, przed błednymi danymi (np. tekst)

# try:
#     except(TypeError):
#     print("Przyjmuję tylko liczby całkowite.")

def max_from_list(*args):
    my_list = list(args)
    my_max = my_list[0]
    indeks = 0
    for n in range(0, len(my_list)):
        try:
            if my_list[n] > my_max:
                my_list[n] = my_max
                indeks = n
        except(TypeError):
            print("Przyjmuję tylko liczby całkowite.")
    return indeks





print(max_from_list(4, 2, 1, 5, "ala", 99, 100))

# my_list = [4, 2, 1, 5, 8, 99, 100]
#
# print(my_list.sort())

# najmniejsza = liczby[0]
#     indeks = 0
#     for n in range(0,len(liczby)):
#         if liczby[n] < najmniejsza:
#             najmniejsza = liczby[n]
#             indeks = n
#     return indeks