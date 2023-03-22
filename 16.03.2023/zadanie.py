# Napisz funkcję, która przyjmuja łańcuch znakowy
#     (dla ułtawienia: same małe litery)
# Przykładowo: alamakotaakotmapierdolca
# Funkcja ma zwrócić słownik (return), który zawiera informacje w postaci:
#     Klucz - litera
#     Wartość - ilość wystąpień litery w tekście
# Przykładowo: dla klucza "l" wartości to 2

txt = "alamakotaakotmapierdolca"

def my_counting (text):
    result = {}
    for c in text:
        if c not in result.keys():
            result[c] = text.count(c)
    return result

print(my_counting(txt))

