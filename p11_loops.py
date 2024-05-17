# while loop
# Bude provádět cykly dokud je n menší než 5
n = 0
while n < 10:
    n += 1  # Zvýší n s každým průchodem cyklu (iterací)
    print(n)

print("-"*80)

n = 0
while n < 10:
    n += 1
    if n == 7:
        break
    print(n)

print("-"*80)

n = 0
while n < 10:
    n += 1
    if n == 7:
        continue
    print(n)

print("End - While")

# for loop
animals = ["Dog", "Cat", "Fish"]

for animal in animals:
    print(animal)

for i in range(1, 11, 2):
    print(i)

print("End - For")

