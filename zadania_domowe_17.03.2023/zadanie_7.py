# Zadanie 07
# Napisać program, gdzie użytkownik podaje n łańcuchów znakowych (ilość n również definiuje wcześniej użytkownik).
# Następnie program zwraca informacje ile łańcuchów znakowych jest unikatowych. :)
# Przykładowo: użytkownik podał n = 3. Następnie podał trzy łańcuchy znakowe: Kot, Pies, Kot.
# Program zwróci informacje, że ilość UNIKATOWYCH łańuchów znakowych to: 2.

m = int(input("Podaj ile łańcuchów znakowych podasz."))
my_list = []

for num in range(0,m):
    my_word = input("Podaj łańcuch znakowy:")
    if my_word not in my_list:
        my_list.append(my_word)
print(len(my_list))

