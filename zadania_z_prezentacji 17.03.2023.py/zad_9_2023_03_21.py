# Stwórz dekorator o nazwie debug, który podczas wywoływania funkcji będzie wyświetlał informacje
# o jej nazwie, przekazanych parametrach oraz zwracanym wyniku.


def debug(func):
    def wrapper(*args, **kwargs):
        suma = func(*args, **kwargs)
        wypis = "" + func.__name__ + " " + "( " + " " + ")" + "zwróciła: ", suma)
        for i in args:
            wypis += i + " "
        for kwargs.items in kwargs:
            wypis += kwargs.items + " "
        return wypis
        # print("Funkcja: ", , (args), dict(kwargs), "zwróciła: ", suma)
        return suma
    return wrapper


@debug
def func1(a, b, c):
    return a + b * c


print(func1(3, b=2, c=4))