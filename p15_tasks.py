"""
Task 1: Faktorial
Lze počítat pouze pro celá nezáporná čísla (0, 1, 2, 3,...)
Uživatel zadá číslo, pokud není celé nezáporné -> chyba.

n! = n * (n-1) * (n-2) * ... * 1
5! = 5 * 4 * 3 * 2 * 1 = 120
1! = 1
0! = 1

8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = ... ?
"""

"""
Task 2: Prime numbers (prvočísla)

Uživatel zadá kladné celé číslo, pokud zadá jinak -> chyba
Program zjistí a vypíše, zda se jedná o prvočíslo.

Prvočíslo = číslo, které má PRÁVĚ dva dělitele (sebe a 1).
https://cs.wikipedia.org/wiki/Prvo%C4%8D%C3%ADslo
"""

"""
Task 3: Bubble sort
Uživatel zadává čísla (0 pro konec).
Čísla se uloží do seznamu a následně toto pole uspořádáme pomocí algoritmu bubble sort.

[5, 6, 8, 1, 3, 0, 4]
[5, 6, 1, 3, 0, 4, 8]
[5, 1, 3, 0, 4, 6, 8]
[1, 3, 0, 4, 5, 6, 8]
[1, 0, 3, 4, 5, 6, 8]
[0, 1, 3, 4, 5, 6, 8]
"""

"""
Task 4: Perfect number (Dokonalé číslo)

Uživatel zadá celé kladné číslo.
Program zjistí, jestli se jedná o dokonalé číslo a vypíše výsledek: https://cs.wikipedia.org/wiki/Dokonal%C3%A9_%C4%8D%C3%ADslo

Dokonalé číslo je v matematice označení pro číslo, u kterého platí, 
že je součtem všech svých dělitelů (kromě sebe samotného). 
Například číslo 6 má dělitele 1, 2, 3 a platí, že 1 + 2 + 3 = 6. 
Dalšími takovými čísly jsou ještě např. 28, 496, 8128. 
28 = 1 + 2 + 4 + 7 + 14

Bonus: 
Abundantní číslo: https://cs.wikipedia.org/wiki/Abundantn%C3%AD_%C4%8D%C3%ADslo
Deficientní číslo: https://cs.wikipedia.org/wiki/Deficientn%C3%AD_%C4%8D%C3%ADslo
"""

"""
Task 5: Temperature (Teplota)
Uživatel zadá teplotu (desetinné číslo) ve °C a program tuto teplotu převede na °F a °K.

Banus:
Uživatel zadá dvě teploty ve °C (dolní a horní mez) a program vypočítá °F a °K v daném rozmezí (krok 1 °C).
Např: uživatel zadá hodnoty 0 a 10, program vypíše:
°C    °F    °K
0     32    ...
1   32.6    ...
2      .
3      . 
4      .
5
6
7
8
9
10

# Převod mezi °C a °F: F = 1,8 * C + 32
# Převod mezi °C a °K: K = C + 273,15
"""