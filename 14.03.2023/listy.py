## Lista

animals = ["Kot", "Pies", "Słoń", "Żółw", "Chomik", "Papuga"]
numbers = [2, 5, 10, 3]
# #metody funkcje listy
# print(len(animal))
# print(animals[0], animals[-1], animals[2:4])
# print(sum(numbers), max(numbers), min(numbers))

# dodawanie
# print(animals.append("szynszyla")) #jeden element
# print(animals)
# animals.extend(["Mysz", "Kanarek"]) #wiele elementów
# print(animals)
# animals.insert(1, "Krokodyl")
# print(animals)
# animals.insert(1, ["a", "b"])
# print(animals)

# usuwanie
# animals.remove("szynszyla")
# print(animals)
# animals.pop()
print(animals)
animals.pop(2)

deleted_value = animals.pop(0)
print(animals, deleted_value)

# Modyfikacja
animals[0] = "Mrówka"
print(animals)