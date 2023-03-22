# # Write a Python program to sum all the items in a list.
# list = [2,4,5,6,7,8,10]
# print(sum(list))

# Write a Python program to get the largest number from a list.
# Write a Python program to get the smallest number from a list.
# list = [2,4,5,6,7,8,10]
# print(max(list))
# print(min(list))

# Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
# Sample_list = ['abc', 'xyz', 'aba', '1221']
# print(len(Sample_list))
#
# print(list.copy(Sample_list))

# Write a Python program to get a list, sorted in increasing order
# Sample_List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(sorted(Sample_List))

# Napisz program, który z listy dni_tyg = ['poniedziałek', 'wtorek',
# 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela'] pobiera wycinek
# z elementów listy o indeksach od 2 do 6.

# dni_tyg = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
# print(dni_tyg[2:6])

# Dana jest lista imiona, która zawiera 4 imiona. Napisz program, który wykorzystując
# metodę index(), zamienia wybrane stare imię na nowe imię. W programie
# zastosowano obsługę sytuacji wyjątkowych

# names = ["Monika", "Dorota", "Zofia", "Małgorzata"]
#
# def name_changer(indx, name):
#     names.pop(indx) and names.insert(indx, name)
#
# name_changer(1, "Doris")
# print(names)

# Dana jest lista imiona zawierająca 4 imiona. Napisz program, który korzystając
# z metody insert(), wstawia nowy element do tej listy w ściśle określonym
# miejscu.

names = ["Monika", "Dorota", "Zofia", "Małgorzata"]

# new_name_indx = int(input("Podaj index. Gdzie mam wstawić nowe imię?"))
# name = str(input("Jakie imię mam wstawić?"))
#
# names.insert(new_name_indx, name)
# print("Tak wygląda teraz lista imion", names)
# names.sort()
# print(names)
# # print(sorted(names))



# Dana jest lista imiona, która zawiera 4 imiona. Napisz program, który korzystając
# z metody remove(), usuwa wybrany element z listy imiona.

# names = ["Monika", "Dorota", "Zofia", "Małgorzata"]
#
# name_to_remo = str(input("Które imię mam usunąć?"))
# names.remove(name_to_remo)
# print(names)

# Dana jest lista imiona, która zawiera 4 imiona. Napisz program, który korzystając
# z metody reverse(), odwraca kolejność elementów na tej liście.

# names = ["Monika", "Dorota", "Zofia", "Małgorzata"]
# print(names)
# names.reverse()
# print(names)

# Napisz program, który z zadanego ciągu tekstowego 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# pobiera pewien dowolny wycinek.

# litery = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# print("To nasze litery", litery)
#
# a = int(input("Podaj numer od 1-26"))
# b = int(input("Podaj numer od 1-26 "))
#
# wycinek = (litery[a:b])
# print(wycinek)

# Napisz program, który testuje ciąg tekstowy za pomocą operatorów in i not in.

zda = "Alicja z krainy czarów."

def check_letter:


