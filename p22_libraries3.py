# import knihovny
# metoda 3: importujeme pouze vybrané funkce,
# nepotřebujeme před funkcí psát math.
from math import factorial#, sqrt

result_fact = factorial(5)
print(result_fact)

result_sqrt = sqrt(16)  # nefunguje, není naimportovaná
print(result_sqrt)
