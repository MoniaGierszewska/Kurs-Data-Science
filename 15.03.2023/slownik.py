# Słownik
contacts = {"Adam": "523652478",
            "Ewelina": "656956854",
            "Marcel": "874896541"}

# print(len(contacts))
# # Dostęp do kluczy
# print(contacts.keys())
# print(contacts.values())
# print(contacts.items())

# if "Adam" in contacts.keys():
#     print("Kontakt istnieje.")

# Dodawanie nowych kluczy
# contacts["Iza"] = "123125124"
# print (contacts)
# contacts["Adam"] = "000000000"
# print(contacts)

# Wyświetlenie wybranej wartości
# print(contacts["Ewelina"])
# print(contacts["Bożydar"])
# print(contacts.get("Bożydar", "Kontakt nie istnieje."))

# Usuwanie kluczy (oraz ich wartości)
# contacts.pop("Adam")
# print(contacts)
# contacts["Mateusz"] = contacts.pop[Ewelina]

def add_contacts (contacts: dict,x: str,y: str): ->None:
    if x in contacts.keys():
        print("Kontakt istnieje")
    if x not in contacts.keys():
        contacts[x]="y" and print("Kontakt dodano")

add_contacts ("Malwina","656956854")
print(contacts)