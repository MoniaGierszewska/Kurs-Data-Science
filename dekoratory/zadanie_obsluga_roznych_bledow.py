# # Napisać program, gdzie użytkownik podaje liczby całkowite i je sumuje.
# # Program działa dopóki użytkownik nie poda liczby ujemnej.
# # Po podaniu liczby ujemnej program wyświetla sumę podanych poprzednich liczb.
#
# print("Program sumuje podane liczby całkowite. Koniec programu następuje po podaniu liczy ujemnej.")
#
# suma = 0
#
# while True:
#     my_numbers = int(input("Podaj liczbę całkowitą: "))
#         if my_numbers < 0:
#             print(suma)
#             break
# try:
#     suma += my_numbers
# except TypeError:
#     suma += my_numbers

n = int(input("Podaj liczbę:"))
summary = 0


while n > 0:
    try:
        summary += n
        n = int(input("Podaj liczbę:"))
    except (ValueError):
        summary += 0


    print(f"suma podanych liczb to: {summary}")