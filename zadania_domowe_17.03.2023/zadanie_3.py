# Zadanie 03
# Użytkownik podaje trzy liczby całkowite.
# Następnie program zwraca informację, która z podanych liczb
# jest największa (dla odważnych - możecie również weryfikować czy dane liczbą są takie same).

print ("Program poda największą z podanych przez użytkownika liczb.")
num_1 = int(input("Podaj pierwszą liczbę całkowitą do porównania:"))
num_2 = int(input("Podaj kolejną liczbę całkowitą do porównania:"))
num_3 = int(input("Podaj ostatnią liczbę całkowitą do porównania:"))

lista_num = [num_1, num_2, num_3]
max_value = max(lista_num)
print("{}".format(max_value))
