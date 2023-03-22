# Napisz program, który zwraca wartość bezwzględną liczby pobranej od użytkownika.
# Program powinien pytać o tę liczbę tak długo, aż nie zostanie ona poprawnie podana.
#
# Pamiętaj, że użytkownik nie zawsze wpisze wartość numeryczną, może też wpisać np. “kalafior”.
# Sprawdź, co wtedy się stanie i pamiętaj o obsłudze wyjątków.


while True:
    try:
        a = int(input("Podaj liczbę: "))
        if a >= 0:
            print("Wartość bezwzględna z", a, "to ", a)
        elif a < 0:
            print("Wartość bezwzględna z", a, "to ", -a)
    except(ValueError):
        ("Przyjmuję tylko liczby!")


