# *args and **kwargs
# here when we add a * before args it helps us provide many positional arguments at ones even though its parameters aren't defined
# ** before the kwargs helps as in the same way with keyword arguments

def super_func(*args , **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1 = 5 , num2 = 10))
