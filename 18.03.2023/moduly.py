#MODUŁY

# fprint jako zaokrąglenie
value = 3.98777773
digit = 200
print(f"Wartość: {value:6.2f}") # zajmuje 6 miejsc (z kropką), 2 po przecinku
print(f"Wartość: {value:.2f}")
print(f"Wartość: {digit:4d}")

#----------------
print("-------------------")
print(f"A: {100:10d}")
print(f"B: {2500:10d}")
print(f"C: {1000000000:10d}")
print("-------------------")