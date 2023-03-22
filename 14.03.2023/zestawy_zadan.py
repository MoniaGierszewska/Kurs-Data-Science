# Program przyjmuje od użytkownika dwie liczby:
#     1. Liczba prawidłowych odpowiedzi (int)
#     2. Liczba pytań (int)
# Następnie program wyświetla odpowiedni komunikat na konsoli zależnie od % prawidłowych odpowiedzi:
#     100% - 90% : 5.0, 89% - 76% : 4.5, 75% - 70% : 4.0
#     69% - 60% : 3.5, 59% - 50% : 3.0, 49% - 0% : 2.0
#
# a = int(input("Podaj liczbę prawidłowych odpowiedzi."))
# q = int(input("Podaj liczbę pytań"))
#
# if 100 == a/q*100 >= 90:
#     print("5.0")
# elif 89 >= a/q*100 >= 76:
#     print("4.5")
# elif 75 >= a/q*100 >= 70:
#     print("4.0")
# elif 69 >= a/q*100 >= 60:
#     print("3.5")
# elif 59 >= a/q*100 >= 50:
#     print("3.0")
# elif 49 >= a/q*100 >= 0:
#     print("2.0")

def show_temp_status(x):
    if x < 36.4:
        return "wychłodzenie"
    elif 36.8 >= x >= 36.4:
        return "norma"
    elif 37.1 >= x >= 36.9:
        return "stan podgorączkowy"
    elif x > 37.1:
        return "gorączka"

print(show_temp_status(37))

