def summary (*args): # *args oznacza upakowanie, dowolna ilość elementów może być przekazane
    print(f"Elements: {args}")
    result = 0
    for i in args:
        result += i
    return result


print(summary(1,2,3,4,5,6))
summary(1,2,3)
summary(1)
summary(1,2,3,5,7,8,11)



def fun_with_option(**kwargs):
    if kwargs.get("power", -1) == -1:
        print("Nie ma opcji potęgi")
    else:
        print(2 ** kwargs.get("power", -1))

    if kwargs.get("sqrt", False):
        print("Chciałeś pierwiastkować?")
    else:
        print("Opcja sqrt jest na false")


def roar_value(prefix:, *args):
    for i in args:
        print(f"{prefix} -> {i}")