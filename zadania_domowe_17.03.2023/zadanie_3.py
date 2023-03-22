# Zadanie 03
# Użytkownik podaje trzy liczby całkowite.
# Następnie program zwraca informację, która z podanych liczb
# jest największa (dla odważnych - możecie również weryfikować czy dane liczbą są takie same).

print ("Program poda największą z podanych przez użytkownika liczb.")
a = int(input("Podaj pierwszą liczbę całkowitą do porównania:"))
b = int(input("Podaj kolejną liczbę całkowitą do porównania:"))
c = int(input("Podaj ostatnią liczbę całkowitą do porównania:"))

lista_num = [a, b, c]
max_value = max(lista_num)
print("{}".format(max_value))

if a == b and b == c:
    print("Liczby są takie same.")
elif a == b:
    print("Liczby A i B są takie same.")
elif a == c:
    print("Liczby A i C są take same.")
elif b == c:
    print("Liczby  B i C są takie same.")
else:
    print("Liczby są różne.")