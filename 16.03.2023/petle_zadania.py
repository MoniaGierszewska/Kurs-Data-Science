# Napisz program, gdzie użytkownik podaje liczbę n (int)
# Następnie program wyświetla wszystkie liczby parzyste od 0 do n (włącznie)

# n = int(input("Podaj liczbę, a ja pokażę liczby parzyste od 0 do Twojej liczby"))
# #
# l=0
# for l in range(n):
#     if l %2 == 0:
#         print(l)
#     n+=1

# Wykorzystując pętle while, program wyświetli wszystkie pierwiastki
# #     liczb od 10 do 2 (włącznie) (n ** 0.5)

# n = 10
# while n >=2:
#     print("Pierwiastek", n, "to", n**0.5)
#     n-=1


# Napisz program, który sumuje wszystkie liczby całkowite z danego przedziału
# Początek i koniec podaje użytkownik
# Np. start = 10, end = 12, wynik - 33

n = int(input("Podaj start"))
m = int(input("Podaj koniec"))
suma=0

for i in range(n,m+1):
    suma+=i

print(suma)
