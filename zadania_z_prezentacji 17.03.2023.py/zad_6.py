# Napisz funkcję, która przyjmuje dwa stringi i sprawdza, czy są swoimi anagramami.
# Na przykład:
# „army” i „Mary”,
# „dzielenia” i „niedziela”,
# „Quid est veritas?” i „Vir est qui adest”,
# „Jim Morrison” i „Mr Mojo Risin”
# „Tom Marvolo Riddle” i „I am Lord Voldemort”



def is_anagram (text1, text2):
    dict_t1={}
    text1 = text1.casefold()
    text2 = text2.casefold()

    for litera in text1:
        if litera.isspace():
            continue
        if litera not in dict_t1:
            dict_t1[litera] = 1
        else:
            dict_t1[litera] += 1
    # print (dict_t1)
    for litera in text2:
        if litera.isspace():
            continue
        if litera in dict_t1:
            dict_t1[litera] -= 1
        else:
            return False
    for klucz in dict_t1:
        if dict_t1[klucz] != 0:
            return False
    return True

txt1 = str(input("Podaj słowo: "))
txt2 = str(input("Podaj 2 słowo: "))

print(is_anagram(txt1, txt2))
