"""
TODO: Násobilka
Vypište tabulku násobilky od 1 do 10:
1	   2	 3	 4	 5	 6	 7	 8	 9	 10
2	   4	 6	 8	10	12	14	16	18	 20
3	   6	 9	12	15	18	21	24	27	 30
4	   8	12	16	20	24	28	32	36	 40
5	  10	15	20	25	30	35	40	45	 50
6	  12	18	24	30	36	42	48	54	 60
7	  14	21	28	35	42	49	56	63	 70
8	  16	24	32	40	48	56	64	72	 80
9	  18	27	36	45	54	63	72	81	 90
10	20	30	40	50	60	70	80	90	100

pomocí vhodného cyklu.

Hint: cykly lze vnořovat (použít cyklus uvnitř cyklu)
"""

"""
TODO: Největší hodnota
Uživatel bude zadávat čísla z klávesnice (0 končí).
Vypiště nejvyšší hodnotu.
"""
number = float(input("Zadej číslo [0 pro konec] "))
highest = None
while number != 0:
    print(f"Zadané číslo: {number}")
    if highest is None or number > highest:
        highest = number
    number = float(input("Zadej číslo [0 pro konec] "))

if highest is None:
    print("Nebylo zadáno žádné číslo")
else:
    print(f"Nejvyšší zadané číslo bylo: {highest}")


"""
num1 = "15"
print(type(num1))
if isinstance(num1, int):
    print(f"{num1} je celé číslo")
elif isinstance(num1, float):
    print(f"{num1} je desetinné číslo")
else:
    print(f"{num1} je type {type(num1)}")
"""


"""
TODO: Druhá největší hodnota
Uživatel bude zadávat čísla z klávesnice (0 končí).
Vypiště druhou nejvyšší hodnotu.
"""

"""
TODO: BMI
Uživatel zadá potřebné hodnoty. Spočítejte jeho BMI a na základě tabulky
https://en.wikipedia.org/wiki/Body_mass_index#:~:text=BMI%2C%20basic%20categories,%E2%89%A5%201.60
zobrazí kategorii.
"""