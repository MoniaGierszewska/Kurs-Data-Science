# Napisać funkcję, która jako argument przyjmuje dowolny łańcuch znakowy, a następnie zwraca słownik
# zliczający ilość wystąpień każdego słowa (kot =/= kota). Podpowiedź możemy użyć metody split(" ").

txt = "kot Ali ma kot kot kot kot ma ma "
# txt.split()
def my_words(txt):
    my_words_dict = {}
    text_spl = txt.lower().split(" ")
    for w in text_spl:
        if w not in my_words_dict.keys():
            my_words_dict[w]=1
        else:
            my_words_dict[w] = my_words_dict[w] +1
    return my_words_dict

print(my_words(txt))