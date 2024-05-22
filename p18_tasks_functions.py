"""
TODO: Task 3: Dancing parabolas

Write a function that will calculate the zeros of the given square function.
For this purpose, you can use the formulas presented here.

Note
We assume movement only in the space of real numbers, complex solutions are not required.
"""


def discriminant(a: float, b: float, c: float) -> float:
    return b**2 - 4*a*c


def dancing_parabolas(a: float, b: float, c: float) -> list:
    result = []
    d = discriminant(a, b, c)
    if d > 0:
        result.append((-b-d**(1/2))/(2*a))
        result.append((-b+d**(1/2))/(2*a))
    if d == 0:
        result.append(-b / (2 * a))
    return result


def dancing_parabolas2(a: float, b: float, c: float) -> tuple:
    d = discriminant(a, b, c)
    if d > 0:
        return (-b-d**(1/2))/(2*a), (-b+d**(1/2))/(2*a)
    if d == 0:
        return tuple(-b / (2 * a))
    return ()


# lze vracet i různé datové typy, ale nedoporučujeme to (vzniká chaos v dalším kódu) -> může způsobovat chyby
def dancing_parabolas3(a: float, b: float, c: float):
    d = discriminant(a, b, c)
    if d > 0:
        return (-b-d**(1/2))/(2*a), (-b+d**(1/2))/(2*a)  # tuple
    if d == 0:
        return -b / (2 * a)  # float
    return None  # None


a = float(input("Zadej a: "))
b = float(input("Zadej b: "))
c = float(input("Zadej c: "))

result = dancing_parabolas(a, b, c)
result2 = dancing_parabolas2(a, b, c)
result3 = dancing_parabolas3(a, b, c)
print(f"result = {result}")
print(f"result2 = {result2}")
print(f"result3 = {result3}")
if len(result) == 0:
    print(f"Rovnice {a}x^2 + {b}x + {c} = 0 nemá řešení v oboru reálných čísel.")
elif len(result) == 1:
    print(f"Rovnice {a}x^2 + {b}x + {c} = 0 má jedno řešení {result[0]}")
else:
    print(f"Rovnice {a}x^2 + {b}x + {c} = 0 má dvě řešení {result[0]}, {result[1]}.")
