# def say_hi(name: str):
#     print(f"hello, {name}")
#
# def get_name(name: str):
#     return say_hi(name)
#
# print(get_name("Piotr"))
#
# print(get_name(say_hi))
#
# def parent():
#     def first():
#         print ("first")
#     def second():
#     print("Second")
#
#     print("pa


def trigger_info(func):
    def wrapper(*args, **kwargs):
        print(f"Wywołano funkcję {func}")
        func(*args, **kwargs)
    return wrapper


@trigger_info
    def my_add(a, b):
        return a + b


@trigger_info
    def my_sub(a, b):
        return a - b


print(my_sub(10,2))