def line_decorator(func):
    def wrapper():
        print(f"----------------")
        func()
        print(f"----------------")
    return wrapper



@line_decorator
def my_date():
    print(f"Dzisiaj jest 19-03-20023")


@line_decorator
def my_course():
    print(f"Kurs to: ARPDataPL9")

my_course()
my_date()