
def print_hello_world():
    print("Hello world from inside the function!")


for i in range(10):
    print(f"i = {i}: ", end="")
    print_hello_world()


def greet_by_name(name):
    print(f"Hello, {name}")


greet_by_name("Petr")
greet_by_name("Martin")

"""
Faktorial - pomocí funkce
Lze počítat pouze pro celá nezáporná čísla (0, 1, 2, 3,...)
Uživatel zadá číslo, pokud není celé nezáporné -> chyba.

n! = n * (n-1) * (n-2) * ... * 1
5! = 5 * 4 * 3 * 2 * 1 = 120
1! = 1
0! = 1

8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = ... ?
"""

print("-"*80)


def fact(n):
    #print(n)
    result = 1
    for i in range(1, n+1):
        result *= i
    print(f"{n}! = {result}")


#fact(5)
#fact(8)

for i in range(10+1):
    fact(i)


print("-"*80)


# funkce, která zjistí, zda je zadané číslo prvočíslo
def is_prime(n):
    if n < 0:
        print("Neřeším záporné hodnoty")
    elif n < 2:
        print(f"Číslo {n} není prvočíslo")
    else:
        if n % 2 == 0:
            print(f"Číslo {n} není prvočíslo")
        else:
            i = 3
            while n % i != 0:
                i += 2
            if i == n:
                print(f"Číslo {n} je prvočíslo")
            else:
                print(f"Číslo {n} není prvočíslo")


#is_prime(25)
for n in range(25):
    is_prime(n)


print("-"*80)


# napište funkci, která vypíše všechny dělitele zadaného čísla:
# např: 6 -> 1, 2, 3, 6
def dividers(n):
    print(f"{n}:", end=" ")
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")
    print()


#num = 24
#dividers(num)  # 1, 2, 3, 4, 6, 8, 12, 24
for i in range(1, 25):
    dividers(i)

num = int(input("Zadej kladné celé číslo: "))
dividers(num)
is_prime(num)

#log(sqrt(2^4))

# dividers()  # TypeError: dividers() missing 1 required positional argument: 'n'


def print_full_name(name: str, surname: str) -> None:
    print(f"{name} {surname}")


print_full_name("Jon", "Snow")
print_full_name(name="Jon", surname="Snow")
print_full_name(surname="Snow", name="Jon")


# Defaultní hodnoty parametru
def greet_by_name(name="anybody"):
    print(f"Hello, {name}")


greet_by_name("Petr")
greet_by_name()
