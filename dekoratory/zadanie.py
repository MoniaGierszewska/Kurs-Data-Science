# Napisać dekorator, dla funkcji która nie przyjmuje żadnych argumentów
# oraz niczego nie zwraca, którego zadaniem jest wyświetlenie po wywołaniu
# funkcji napisu "--- KONIEC ---"

# Sprawdzić w praktyce dla dowolnej utworzonej przez Was funkcji.

def end_tell(func):
    def wrapper():
        func()
        print(f"---KONIEC---")
    return wrapper


@end_tell
def my_date():
    print(f"Dzisiaj jest 19-03-20023")


my_date()
