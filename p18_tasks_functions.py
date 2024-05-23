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

# TODO: Task - print_square: funkce vykreslí čtvereček do terminálu pomocí znaku '#' o velikosti zadané v parametru
"""
print_square(1):
#

print_square(2):
##
##

print_square(3):
###
# #
###

print_square(4):
####
#  #
#  #
####
"""

# TODO: Task - print_diamond: funkce vykreslí kosočtverec do terminálu pomocí znaku '#' o velikosti zadané v parametru
"""
print_diamond(1):
#

print_diamond(2):
 #
# #
 #

print_diamond(3):
  #
 # #
#   #
 # #
  #

print_diamond(4):
   #
  # #
 #   #
#     #
 #   #
  # #
   #
"""

# TODO: Bonus - print_circle: funkce vykreslí kružnici do terminálu pomocí znaku '#' o velikosti zadané v parametru
"""
print_circle(1):
#

print_circle(2):
 #
# #
 #

print_circle(20):
           #
        #     #
      #         #
     #           #
      ...
"""


# TODO: prime_numbers(n): funkce vrátí seznam všech prvočísel do zadaného čísla n (včetně)
"""
prime_numbers(10) -> [2, 3, 5, 7]
prime_numbers(30) -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
"""


def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**(1/2)+1), 2):
        if n % i == 0:
            return False
    return True


def prime_numbers(n):
    result = []
    for i in range(2, n+1):
        if is_prime(i):
            result.append(i)
    return result


n = 30
print(f"prime_numbers({n}) = {prime_numbers(n)}")


# TODO: prime_numbers2(n): funkce vrátí seznam n prvních prvočísel
"""
prime_numbers(4) -> [2, 3, 5, 7]
prime_numbers(10) -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
"""
def prime_numbers2(n):
    result = []
    i = 2
    while len(result) < n:
        if is_prime(i):
            result.append(i)
        i += 1
    return result


n = 10
print(f"prime_numbers2({n}) = {prime_numbers2(n)}")

import sys
print(f"sys.maxsize = {sys.maxsize}")


# TODO: task - Fibonacci (Fibonacciho posloupnost)
"""
0  1  2  3  4  5  6   7
0, 1, 1, 2, 3, 5, 8, 13, ...

Napište funkci, která vrátí prvních n čísel Fibonacciho posloupnosti
https://cs.wikipedia.org/wiki/Fibonacciho_posloupnost
"""
def fib(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    result = [0, 1]
    while len(result) < n:
        result.append(result[-2] + result[-1])
    return result


n = 20
print(f"fib({n}) = {fib(n)}")


# TODO: Task - Twin prime (Prvočíselné dvojčata)
"""
Vytvořte funkci, která vrátí prvních n prvočíselných dvojčat: https://cs.wikipedia.org/wiki/Prvo%C4%8D%C3%ADseln%C3%A1_dvojice

def twin_prime(n: int) -> list:
twin_prime(4) -> [(3, 5), (5, 7), (11, 13), (17, 19)]
"""
def twin_prime(n: int) -> list:
    pass


n = 10
print(f"twin_prime({n}) = {twin_prime(n)}")


# TODO: Integer factorization (Prvočíselný rozklad): https://cs.wikipedia.org/wiki/Prvo%C4%8D%C3%ADseln%C3%BD_rozklad
"""
Napište funkci, která pro zadané číslo vrátí seznam prvočíselného rozkladu:
factorization(2) = [2]
factorization(3) = [3]
factorization(4) = [2, 2]
factorization(5) = [5]
factorization(6) = [2, 3]
factorization(7) = [7]
factorization(8) = [2, 2, 2]
factorization(9) = [3, 3]
factorization(10) = [2, 5]
factorization(11) = [11]
factorization(12) = [2, 2, 3]
"""

