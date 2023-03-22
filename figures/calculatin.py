def my_add(a, b):
    return str(a+b)

def my_sub(a,b):
    return str(a-b)

def my_div(a,b):
    if a==0 or b == 0:
        print("Nie dziel cholero przez zero!")
    return str(a/b)

print(my_add(2,5))
print(my_sub(5,-8))
print(my_div(2,1))