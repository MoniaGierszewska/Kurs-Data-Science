# Napisz program, który oblicza pole prostokąta. Wartości boków a i b są typu
# float i należy je wprowadzić z klawiatury. Wynik działania programu należy
# wyprowadzić na ekran komputera.

# a=float(input("Podaj długość boku prostokąta:"))
# b=float(input("Podaj długość drugiego boku:"))
# pole=a*b
# print("Pole prostokąta o boku a:", a, "oraz boku b:", b, "wynosi:", pole)

# Napisz program, który oblicza resztę z dzielenia całkowitego dwóch liczb całkowitych
# a = 37 i b = 11.
#
# print("Program oblicza resztę z dzielenia 2 liczb całkowitych.")
# print("liczba a = 37.")
# print("Liczba b = 11")
# print("Reszta z dzielenia 37/11 wynosi", 37%11, ".")

#Napisz program, który dla trzech liczb a, b i c wprowadzonych z klawiatury
#sprawdza, czy są to trójki pitagorejskie. Dodatkowo należy założyć, że a > 0,
#b > 0 i c > 0.


# Napisz program, który za pomocą instrukcji while dla danych wartości x
# rosnących od 0 do 10 oblicza wartość funkcji y = 3x.

# x=0
# y=0
# while x <=10:
#     y=3*x
#     print("x=", x, "y=", y)
#     x+=1

# Napisz program, który za pomocą instrukcji while wyświetla wszystkie liczby
# całkowite od 1 do 20.

# x=1
# while x <=20:
#     print(x)
#     x+=1

# Napisz program, który korzystając z instrukcji while, sumuje liczby parzyste
# od 1 do 100

# x = 1
# suma = 0
# while x <= 100:
#     if (x %2 == 0):
#         suma += x
#     x+=1
# print(suma)

# Napisz program, który za pomocą instrukcji while sumuje wszystkie liczby
# całkowite od 1 do 100.

x=1
suma=0

while x <= 100:
    suma += x
    x += 1

print(suma)