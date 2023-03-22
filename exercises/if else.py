# Napisz program, który korzystając z konstrukcji if-else, porównuje ze sobą
# dwa imiona: Mirek i Marek.

name1 = 'Mirek'
name2 = 'Marek'

name1_dict = {}

for l in name1:
    if l not in name1_dict.keys:
      name1_dict[l] = name1_dict.keys
    else:
        name1_dict.keys[l] += 1

    print(name1_dict)

for k in name2:
    if k in name1_dict.keys:
        name1_dict.keys[k] -= 1
    else:
        print("imiona są inne")
