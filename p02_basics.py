# Data types in Python

# číselné
var_int = 5  # int = integer = celé číslo
var_float = 0.587  # float = desetinné číslo # pozor, musí být použite desetinná tečka!
var_complex = (1-6j)  # complex = komplexní číslo # 1-6i https://cs.wikipedia.org/wiki/Komplexn%C3%AD_%C4%8D%C3%ADslo

# textové
var_str = "ahoj"  # str = string = řetězec
var_bytes = b"ahoj"  # bytes

# pravdivostní
var_bool = True  # bool = boolean = pravdivostní hodnota True/False (Pravda/Nepravda)

# nedefinované
var_NoneType = None  # NoneType = nedefinovaný typ

print(var_int)


num1 = 17
text = "ahoj"
num2 = 99

print("Text")
print(-19)
print(var_float)
print(var_bool)
print(var_NoneType)

num1 = 10
print(num1)
print(type(num1))  # <class 'int'>
num1 = "deset"
print(num1)
print(type(num1))  # <class 'str'>
num1 = 'jedenáct'
print(num1)

# lze používat jednoduché i dvojité uvozovky pro definici stringu
text1 = "text obsahuje jednoduché uvozovky 'ukázka'"
print(text1)
text1 = 'text obsahuje dvojité uvozovky "ukázka"'
print(text1)

# function type()
num1 = 1
num2 = 2
print(type(num1))  # <class 'int'>
print(type(num2))  # <class 'int'>
print(f"{num1} + {num2} = {num1+num2}")

num1 = "1"
num2 = "2"
print(type(num1))  # <class 'str'>
print(type(num2))  # <class 'str'>
print(f"{num1} + {num2} = {num1+num2}")

num1 = 1
num2 = "2"
print(type(num1))  # <class 'int'>
print(type(num2))  # <class 'str'>
#print(f"{num1} + {num2} = {num1+num2}")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(type(var_float))  # <class 'float'>
print(type(var_bool))  # <class 'bool'>

# Python funguje na unicode, lze teoreticky v názvech používat diakritiku
# ale velmi toto NEDOPORUČUJEME
# raději používat anlické názvy
proměnná = 10
print(proměnná)

# proměnné jsou case sensitive = citlivé na velikost
num_a = 10
num_A = 20
print(f"num_a = {num_a}")
print(f"num_A = {num_A}")

# 01_num = 5 nelze začínat název číslicí

# snake_case používáme por názvy proměnných a funkcí
# CamelCase používáme pro názvy tříd
# CONSTANT používáme pro konstanty


number: int = "5"  # můžeme definovat typ, ale Python na to nebere ohled
print(type(number))
number = "pět"
print(number)

# Komentáře v Pythonu
# jednořádkový komentář pomocí znaku #
num = 5  # od znaku # do konce řádku je komentář

"""
Víceřádkový
komentář
"""

# Keyword
#import = "import"  # SyntaxError: invalid syntax


# Operators
## Arithmetic operators = aritmetické operace, tj. na číslech
num1 = 16
num2 = 4
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")  # násobení
print(f"{num1} ** {num2} = {num1 ** num2}")  # mocnina 10^2
print(f"{num1} / {num2} = {num1 / num2}")  # dělení, vrací float
print(f"{num1} // {num2} = {num1 // num2}")  # celočíselné dělení, vrací int, pozor, vrací menší celé číslo, např. -20 // 7 = -3
print(f"{num1} % {num2} = {num1 % num2}")  # modulo = zbytek po celočíselném dělení, např. -20 % 7 = 1
print(f"{num1} ** (1/{num2}) = {num1 ** (1/num2)}")  # odmocnina

## Comparison operators = porovnání => výsledkem bude bool (pravdivostní hodnota True/False)
num1 = 10
num2 = 10
print(f"{num1} == {num2}: {num1 == num2}")  # shoda (rovná se): 10 == 10: True x 10 == 20: False
print(f"{num1} != {num2}: {num1 != num2}")  # neshoda (nerovná se): 10 != 10: False
print(f"{num1} < {num2}: {num1 < num2}")  # menší než: 10 < 20: True
print(f"{num1} > {num2}: {num1 > num2}")  # větší než
print(f"{num1} <= {num2}: {num1 <= num2}")  # menší rovno: 10 <= 10: True
print(f"{num1} >= {num2}: {num1 >= num2}")  # větší rovno: 10 >= 10: True

## Assignment operators = přiřazování
num1 = 10
print(f"num1 = {num1}")
num1 += 5  # num1 = num1 + 1 # do dané proměnné přičti hodnotu
print(f"num1 = {num1}")
num1 -= 7  # odečte hodnotu
print(f"num1 = {num1}")
num1 *= 2
print(f"num1 = {num1}")
num1 **= 2
print(f"num1 = {num1}")
num1 /= 16
print(f"num1 = {num1}")
num1 //= 5
print(f"num1 = {num1}")
num1 %= 2
print(f"num1 = {num1}")

### bitové operace
# var1   var2   AND    OR     XOR
# True   True   True   True   False
# True   False  False  True   True
# False  True   False  True   True
# False  False  False  False  False
truth = True
truth &= False  # konjunkce, logické A (and)
print(f"truth = {truth}")  # True and False = False
truth = True
truth |= False  # disjunkce, logické nebo (or): alespoň jedna je pravdivá
print(f"truth = {truth}")  # False or True = True
# znak | lze napsat pomocí ctrl+alt+w na české klávesnici
truth = True
truth ^= True   # výlučné nebo, XOR: právě jedna je pravdivá
print(f"truth = {truth}")

### bitové posuny: https://cs.wikipedia.org/wiki/Bitov%C3%A1_operace
#            16 8 4 2 1
num1 = 8    #   1 0 0 0 = 8
num1 <<= 1  # 1 0 0 0 0 = 16
print(f"num1 = {num1}")
#            32 16 8 4 2 1
num1 = 32  #  1  0 0 0 0 0 = 32
num1 >>= 2 #       1 0 0 0 = 8
print(f"num1 = {num1}")

# 4 2 1
# r w x
# 1 0 0 = 4
# 0 1 0 = 2
# 0 0 0 = 0
# 1 1 1 = 7
# 1 1 0 = 6
num1 = 5  # 101
if (num1 % 2 == 1):
    print("mám právo pro spuštění (x)")
else:
    print("nemám právo pro spuštění (x)")
num1 >>= 1
if (num1 % 2 == 1):
    print("mám právo pro zápis (w)")
else:
    print("nemám právo pro zápis (w)")
num1 >>= 1
if (num1 % 2 == 1):
    print("mám právo pro čtení (r)")
else:
    print("nemám právo pro čtení (r)")

## Identity operators
# is, is not
truth = True
print(f"{truth} is True = {truth is True}")
print(f"{truth} is not True = {truth is not True}")

## Logical operators
truth1 = True
truth2 = False
print(f"{truth1} and {truth2} = {truth1 and truth2}")
print(f"{truth1} or {truth2} = {truth1 or truth2}")
print(f"not {truth1} = {not truth1}")  # negace: not True = False, not False = True


## Membership operators
array = [1, 2, 3]
num = 2
print(f"{num} in {array} = {num in array}")  # test, zda je prvek v seznamu
print(f"{num} not in {array} = {num not in array}")  # test, zda prvek není v seznamu
print("fox" not in "cow, dog, cat")
print("great" in "Python is great!!!")


## Bit operators
truth1 = True
truth2 = True
# and = "a zároveň" (platí obě podmínky)
print(f"{truth1} & {truth2} = {truth1 & truth2}")
print(f"{truth1} and {truth2} = {truth1 and truth2}")
# or = "nebo" (platí alespoň jedna podmínka)
print(f"{truth1} | {truth2} = {truth1 | truth2}")
print(f"{truth1} or {truth2} = {truth1 or truth2}")
# xor = "výlučné nebo" (platí právě jedna podmínka)
print(f"{truth1} ^ {truth2} = {truth1 ^ truth2}")
# not = negace
print(f"not {truth1} = {not truth1}")

num1 = 8
print(f"{num1} << {1} = {num1 << 1}")
print(f"{num1} >> {1} = {num1 >> 1}")


# Text concatenation
name = "John"
greeting = "Hello, " + name
print(greeting)
joe = "Joe"
jane = "Jane"
print(joe + " and " + jane)

# Repetition of text
message = "Hi"
print(message * 2)
new_message = "Hi" * 5
print(new_message)
number = 3
message = message * number
print(message)
print("-" * 80)

num1 = 5
num2 = "6"
print(f"{num1} + {num2} = {num1 + int(num2)}")

# print(f"{num1} + {num2} = {num1 + num2}")
