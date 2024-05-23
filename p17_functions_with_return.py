def calculate_square(a):
    return a * a
    print(a*a)  # nedosažitelný kód (je za return)


num = 5
print(f"{num}^2 = {calculate_square(num)}")
print(f"{num}^2 + 1 = {calculate_square(num) + 1}")


def fact(n: int) -> int:
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(f"{num}! = {fact(num)}")
fact_5 = fact(5)
fact_7 = fact(7)
print(f"5! = {fact_5}, 7! = {fact_7}, 5! + 7! = {fact_5 + fact_7}")


def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n, 2):
        print(f"Zkouším dělit číslem {i}")
        if n % i == 0:
            return False
    return True


num = 19
if is_prime(num):
    print(f"Číslo {num} je prvočíslo")
else:
    print(f"Číslo {num} není prvočíslo")


def dividers(n: int) -> list:
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result


num = 36
print(f"{num}: {dividers(num)}")

if not is_prime(num):
    print(f"{num}: {dividers(num)}")


# funkce pro nalezení největšího společného dělitele dvou čísel
# gcd(16, 24) -> 8
def gcd(n1: int, n2: int) -> int:
    dividers1 = dividers(n1)
    dividers2 = dividers(n2)
    """for i in range(len(dividers1)-1, 0, -1):
        if dividers1[i] in dividers2:
            return dividers1[i]"""
    for divider in dividers1[::-1]:
        if divider in dividers2:
            return divider
    return 1


num1 = 20
num2 = 24
print(f"{num1}: {dividers(num1)}")
print(f"{num2}: {dividers(num2)}")
print(f"Největší společný dělitel čísel {num1} a {num2} je {gcd(num1, num2)}")


# TODO: Task lcm = nejmenší společný násobek: https://cs.wikipedia.org/wiki/Nejmen%C5%A1%C3%AD_spole%C4%8Dn%C3%BD_n%C3%A1sobek
