# numb= int(input("Podaj liczbę:"))
# if numb %2 == 0:
#     print("liczba jest parzysta")
# else:
#     print ("liczba jest nieparzysta")

numb= int(input("Podaj liczbę:"))

if (numb%3)==0 and (numb%5)==0:
    print("Pif Paf")
elif (numb%3)==0:
    print("Pif")
elif (numb%5)==0:
    print("Paf")
else:
    print("Twoja liczba to:", numb, "nie spełnia warunku")