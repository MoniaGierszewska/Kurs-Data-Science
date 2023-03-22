# Napisz funkcję manage_list, która przyjmuje dwa argumenty:
#     - Opcja: dodaj, usun
#     - Wartość
# Jeżeli wybraliśmy dodaj, wykonany jest append
# Jeżeli usun - wykonujemy pop()
# Funkcja niczego nie zwraca

animals = ["Kot", "Pies", "Słoń", "Żółw", "Chomik", "Papuga"]

# add=input("Podaj czy chcesz dodać '1' czy usunąć '2'?")

def manage_list(action, value):
    if action == 1:
        animals.append(value)
    elif action == 2:
        if value in animals:
            animals.pop(animals.index(value))
    else:
        print("Nie ma takiej wartości!")

manage_list(2,"Żaba")
print(animals)


