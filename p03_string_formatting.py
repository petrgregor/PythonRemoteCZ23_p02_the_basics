# String formatting

## Without any formatting.
print("Hi")
number = 15.7
print(number)
### Display several values at once.
print("Hello", "World!")
### Define the separator between the values (parameters) given to it.
print("Hello", "World!", sep=", ")  # můžeme předefinovat oddělovač položek (defaultně mezera)
print("number =", number)
array = [1, 2, 3, 4]
print(array)
### Add a string after the last value.
print("Ahoj", end=" ")  # můžeme předefinovat konec (defaultně konec řádku)
print("světe!")
print("Na novém řádku.")
print("Text a pod ním bude prázdný řádek", end="\n\n")
print("Text pod prázdným řádkem")
print("První", "Druhý", "Třetí", "Čtvrtý", sep="\t")
print("Ahoj", "Hello", "Hi\t", "Nazdar", sep="\t")

### Displaying multiple strings at once
print("What ", "a ", "beautiful ", "day", ".", sep="")
print("1", "2", 3, 4, 5)
fruit = "orange"
print("apple", "banana", fruit)

### Displaying multiple strings with a separator simultaneously
print("What", "a", "beautiful", "day", ".", sep="-")
print("1", "2", 3, 4, 5, sep=" < ")
fruit = "orange"
print("apple", "banana", fruit, sep=" + ")

### Displaying multiple strings simultaneously with a separator and final string
print("What", "for", "beautiful", "day", ".", sep="-", end="!\n")
print("1", "2", 3, 4, 5, sep="<", end="<...\n")
fruit = "orange"
print("apple", "banana", fruit, sep="+", end=" = yummy\n")

print("What", "for", "beautiful", "day", end="")
print(".")

## The printf formatting from the C language - an older solution.
title = "General"
name = "Kenobi"
print("Hello there, %s %s." % (title, name))
print("Hello there, ", title, " ", name, ".", sep="")

## The str.format() formatting - a newer solution.
title = "General"
name = "Kenobi"
print("Hello there, {} {}.".format(title, name))
print("Hello there, {title} {name}.".format(name=name, title=title))
print("Hello there, {1} {0}.".format(name, title))

print("Hello there, {} {} {}.".format(title, title, name))
print("Hello there, {title} {title} {name}.".format(name=name, title=title))
print("Hello there, {1} {1} {0}.".format(name, title))

## The f-string interpolation - the latest solution.
title = "General"
name = "Kenobi"
print(f"Hello there, {title} {name}.")

num1 = 2
num2 = 7
result = (num1 * num2) ** 2
print(f"{num1} times {num2} to the power of 2 is {result}")
print(f"{num1} times {num2} to the power of 2 is {(num1 * num2) ** 2}")

header1 = "Name"
header2 = "Age"
name = "John"
age = 22

print(f"| {header1} | {header2} |")
print("-" * 27)
print(f"| {name} | {age} |")
print()  # prázdný řádek

### https://www.utf8-chartable.de/unicode-utf8-table.pl?start=9472&unicodeinhtml=dec
print("┌", "─" * 4, "┬", "─" * 4, "┐")
print(f"│ {header1} │ {header1} │")
print("├", "═" * 4, "┼", "═" * 4, "┤")
print(f"│ {name} │  {age}  │")
print("└", "─" * 4, "┴", "─" * 4, "┘")

# Changing the way the variable is displayed
n = 109.2345654324
print(f"n = {n: .3f}")
number3 = 10 / 3  # 3.3333333
print(f"number3 = {int(number3)}")
print(f"number3 = {number3: .0f}")
print(f"number3 = {number3: .3f}")
number3 = int(number3)
print(f"number3 = {number3: .5f}")
number4 = 10.0
print(f"number4 = {number4: .5f}")

percent = 0.71
print(f"percent = {percent: .0%}")
print(f"percent = {percent: .1%}")

# Basic operations on strings
## The len() function = délka řetězce
sentence = "Hello, beautiful World!"
print(f"len(sentence) = {len(sentence)}")

## The .index() function = najde index prvního výskytu daného znaku
print(f"sentence.index('o') = {sentence.index('o')}")
# print(f"sentence.index('S') = {sentence.index('S')}")  # ValueError: substring not found

## The .count() function = vrátí počet výskytů
print(f"sentence.count('o') = {sentence.count('o')}")
print(f"sentence.count('l') = {sentence.count('l')}")
print(f"sentence.count('S') = {sentence.count('S')}")

## Extracting a single character from the string
print(f"sentence[7] = {sentence[7]}")
print(f"sentence ends with '{sentence[len(sentence)-1]}'")
print(f"sentence ends with '{sentence[-1]}'")

## String slicing
hello = "Hello, World!"
#   H  e  l  l  o  ,  _  W  o  r  l  d  !
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13
#                      -6 -5 -4 -3 -2 -1 0
print(f"hello[7:12] = {hello[7:12]}")
print(f"hello[-3] = {hello[-3]}")
print(f"hello[-2:-7:-1] = {hello[-2:-7:-1]}")

# String slicing without some characters
print(f"hello[7:12:2] = {hello[7:12:2]}")

# Reversing the string
print(f"Reverse: '{hello[::-1]}'")

# The .upper() function
print(f"Upper: {hello.upper()}")

# The .lower() function
print(f"lower: {hello.lower()}")

