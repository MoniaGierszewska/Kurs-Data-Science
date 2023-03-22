# Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową, np.:
# 112 - > „jeden jeden dwa”
# 9973 -> „dziewięć dziewięć siedem trzy”
# Podpowiedź: potrzebujesz funkcji input(), słownika oraz pętli.

given_num = input("Podaj liczbę:")

numb_dict = {0 : "zero", 1 : "jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"pięć", 6:"sześć", 7:"siedem", 8:"osiem", 9:"dziewięć"}

txt = ""

for n in given_num:
    txt += numb_dict[int(n)] + " "
print(txt)
