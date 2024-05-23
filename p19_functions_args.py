# Functions with any number of arguments - args

# Add any number of numbers
def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result


print(add(100))
print(add(5, 10))
print(add(1, 2, 3, 4, 5))  # Prints 15


# Prints the name and what the user gives
def print_name_and_something(name, *strings):
    print(f"First name: {name}")
    for string in strings:
        print(string)


print_name_and_something("Petr", "first", "second", "third")


# Functions with any number of arguments - kwargs

# Add any number of ingredients
def add_ingredients(**kwargs):
    result = 0
    for key in kwargs:
        result += kwargs[key]
    return result


print(add_ingredients(eggs=3, spam=5, cheese=2))  # Will print 10


# Functions with any number of arguments - args and kwargs

# Add any number of ingredients
def add_ingredients(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for key in kwargs:
        result += kwargs[key]
    return result


print(add_ingredients(1, 2, 3, eggs=3, spam=5, cheese=2))  # Will print 16


# Examples
def is_prime(*args) -> list:
    result = []
    for n in args:
        if n == 2:
            result.append(True)
        elif n % 2 == 0:
            result.append(False)
        else:
            prime = True
            for i in range(3, int(n**(1/2)+1), 2):
                if n % i == 0:
                    prime = False
            result.append(prime)
    return result


print(f"{is_prime(2, 5, 7, 9, 10, 5, 12)}")
print(f"{is_prime(29)}")
print(f"{is_prime()}")


# Task: multiply
"""
napište funkci multiply, která vynásobí všechny zadané argumenty a vrátí výsledek

multiply() -> 0
multiply(5) -> 5
multiply(2, 5) -> 10
multiply(1, 2, 3) -> 6
"""
def multiply(*args):
    if not args:
        return 0
    result = 1
    for arg in args:
        result *= arg
    return result


print(f"{multiply()}")
print(f"{multiply(5)}")
print(f"{multiply(2, 5)}")
print(f"{multiply(1, 2, 3)}")
print(f"{multiply(10, 255, 0)}")


# TODO: squares
"""
definujte funkci print_squares, která bude brát libovolný počet argumentů
a pro každý zadaný argument vykreslí čtverec
"""

# TODO: factorizations
"""
Předefinujte funkci factorization tak, aby brala libovolný počet argumentů,
pro každý argument provede faktorizaci a vrátí seznam všech výsledků

factorizations(10, 11, 12) -> [[2, 5], [11], [2, 2, 3]]
protože:
factorization(10) = [2, 5]
factorization(11) = [11]
factorization(12) = [2, 2, 3]
"""