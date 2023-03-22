x = 10
try:
    print(x / 0)
except (ZeroDivisionError, TypeError):
    print("Probowałeś dzielić przez zero.")
finally:
    print("WYKONAŁEM SIĘ!") #wykonaj to zawsze na końcu - niezależnie od powyższych bloków


a = [10, 20, 3, 4, "Ala ma kota", True, 3, 4, 12, "Piesek"]

for i in range(len(a)):
    try:
        a[i] = dec_to_bin(a[i])
    except TypeError:
        errors_value.append(a[i])

