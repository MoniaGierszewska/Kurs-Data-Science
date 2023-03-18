# Napisać funkcję, która zamienić stopnie Celsjusza na Kelwina. Funkcja przyjmuje jako argument
# temperaturę w C, a funkcja zwraca temperaturę w K. Więcej informacji o konwersji:
# https://www.rapidtables.org/pl/convert/temperature/how-celsius-to-kelvin.html
# Obie wartości maja być typu float


def celc_kalwin (temp: float):
    return temp + 273.15

print(celc_kalwin(24))