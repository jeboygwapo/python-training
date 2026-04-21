# Unlimited arguments
# def add(*args):
#     print(args[-1])
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
# print(add(15,15,14,13,123,12))

# Keyword arguments or **kwargs
def calculate(n, **kwargs):
    # print(kwargs)
    # for k,v in kwargs.items():
    #     print(k,v)
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)
print(my_car.colour)
print(my_car.seats)