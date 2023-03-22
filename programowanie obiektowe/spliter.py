# start - godzina rozpoczęcia seansu
# playtime - ile sekund oglądaliśmy

# Program ma podzielić playtime na poszczególne grupy.

# p = 3.5
# s = 5.6
#
# 5: 0.4 (do 6)
# 6: 1.0 (do 7)
# 7: 1.0 (do 8)
# 8: 1.0 (do 9)
# 9: 0.1 (do 10) <-- p + s
#
# 0: 0.0 - 1.00
# 1: 1.01 - 2.00
# 2: 2.01 - 3.00
# ...
# 10: 10.01 - 11.00
#
# start_watching = 5.6
# time_watching = 3.5
#
# end_watching = 9.1
# hour_dict = {0 : 1, 1 : 1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
#
# for w in range(0:4):
#     w/w
#     if w not in my_words_dict.keys():
#         my_words_dict[w] = 1
#     else:
#         my_words_dict[w] = my_words_dict[w] + 1

def time_split (start, palytime):
    end = start + playtime

while start <= end:
    if int(start) + 1 > end:
        print(f"{int(start)} - {end - start:.1f}")
    else:
        print(f"{int(start)} - {(int(start) +1) - start:.1f}")
    start = int(start) +1


time_split(5.6, 3.5)