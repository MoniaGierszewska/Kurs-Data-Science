# Write a Python program to calculate the length of a string.
#
# x = str(input("Podaj zdanie a obliczę jego długość."))
# print(len(x))

# Write a Python program to get a single string from two given strings, separated by a space
# and swap the first two characters of each string.

# x = str(input("Podaj pierwszy wyraz."))
# y = str(input("Podaj drugi wyraz."))
# print(y, x)

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead. If the string length of the given
# string is less than 3, leave it unchanged.

# x = str(input("Podaj wyraz (min. 3 litery)."))
#
# if len(x) <= 2:
#     print("Wyraz",x,"jest za krótki!")
# elif x.endswith("ing"):
#     print(str(x+"ly"))
# else:
#     print(str(x+"ing"))

# Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string. Sample String : 'The lyrics is not that poor!'

x = str(input("Podaj zdanie"))

y = x.find("not")
z = x.find("poor")

print(y)
print(z)

if z>y:
    print(x.replace("not poor","good"))

