with open ("reduta.txt", "r", encoding="utf-8") as file:
    reduta_dict={}
    for line in file:
        for word in line.replace("\n", "").split(" "):
            if word in reduta_dict.keys():
                reduta_dict[word] += 1
            else:
                reduta_dict[word] = 1
        print(reduta_dict)