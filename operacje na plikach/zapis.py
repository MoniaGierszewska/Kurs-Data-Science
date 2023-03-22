n= int(input("Podaj ile losowań wykonać: "))
from random import randint

for i in range(n):
    numbers = set()
    while len(numbers) < 6:
        numbers.add(f"{randint(1,49)} ")

    with open("lotto.txt", "a+", encoding="utf-8") as file:
        file.writelines(numbers)
        file.write("\n")



