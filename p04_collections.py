# Collections

## List = seznam
alphabet = []  # prázdný seznam
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Length of alphabet is {len(alphabet)}.")
print(f"Length of numbers is {len(numbers)}.")

alphabet.append("a")
alphabet.append("b")
alphabet.append("c")
print(f"Length of alphabet is {len(alphabet)}.")
print(f"alphabet = {alphabet}")

print(f"The first item in alphabet is: '{alphabet[0]}'.")

alphabet.extend(["f", "d", "g", "e"])
print(f"Alphabet: {alphabet}, (length: {len(alphabet)})")

# funkce sorted uspořádá hodnoty ale nemění požadí v seznamu
print(f"Sorted alphabet: {sorted(alphabet)}")
sorted_alphabet = sorted(alphabet)
print(f"Alphabet: {alphabet}, (length: {len(alphabet)})")
print(f"Sorted alphabet: {sorted_alphabet}")

alphabet.sort()  # metoda .sort() mění seznam (uspořádá)
print(f"Alphabet: {alphabet}, (length: {len(alphabet)})")

names = ["Petr", "Petr", "Martin", "Zdena", "Adolf", "Řehoř", "Cyril", "Bedřich", "Pavel", "Chavier"]
names.sort()
print(f"names = {names}")  # POZOR: je to dle UTF-8 tabulky, ne správně česky

print(f"names[0:3]: {names[0:3]}")
print(f"names[1:5]: {names[1:5]}")
print(f"names[3]: {names[3]}")
print(f"names[2:]: {names[2:]}")
print(f"names[:5]: {names[:5]}")
print(f"names[:]: {names[:]}")
print(f"names[::2]: {names[::2]}")
print(f"names[1::2]: {names[1::2]}")
print(f"names[::-1]: {names[::-1]}")
print(f"names[::-2]: {names[::-2]}")

### do seznamu můžeme vkládat cokoliv
new_list = [1, "jedna", 1.1, [2, "dva"]]
print(f"new_list = {new_list}")

## Dictionary = slovník, klíč musí být unikátní
phonebook = {}  # prázdný slovník
dictionary = {
    'Petr': 'Gregor',
   # 'Petr': 'Novák',  # nelze mít duplicitní klíč (key)
    'Marek': 'Ztracený'
}

phonebook["John"] = 11122233
phonebook["Jack"] = 44455666
print(f"phonebook = {phonebook}")

### Deleting items from the dictionary
jack = phonebook.pop("Jack")
print(f"Jack = {jack}")
print(f"phonebook = {phonebook}")
del phonebook["John"]
print(f"phonebook = {phonebook}")

print(f"Petr: {dictionary.get("Petr")}")
print(f"Marek: {dictionary.get("Marek")}")
print(f"Martin: {dictionary.get("Martin", "<undefined>")}")

phonebook2 = {
    'Petr': [1112233, 44455566],
    'Martin': 777888999,
    'Radka': "nemá"
}
print(f"Petr: {phonebook2.get("Petr")}")
print(f"Petr: {phonebook2.get("Petr")[0]}, {phonebook2.get("Petr")[1]}")

## Tuple
tuple1 = ()  # prázdný tuple
tuple2 = ("dog", "cat", 2000, 5.0, True, [1, 2, 3])
print(f"tuple2 = {tuple2}")
tuple3 = "jedna", "dvě", 3
print(f"tuple3 = {tuple3}")
print(f"tuple2[2:4] = {tuple2[2:4]}")

## Set = množina - nezáleží na pořadí, každý prvek pouze jednou
animals = {"dog", "cat", "elephant", "dog"}
print(f"animals = {animals}")

empty_set = set()
print(f"empty_set = {empty_set}")
empty_set.add("a")
print(f"empty_set = {empty_set}")

animals.add("mouse")
print(f"animals = {animals}")
animals.update(["bird", "horse"])
print(f"animals = {animals}")
animals.add("mouse")
print(f"animals = {animals}")
animals.remove("mouse")
print(f"animals = {animals}")
# animals.remove("mouse")  # KeyError: 'mouse': nelze odebrat položku, která v množině není
animals.discard("mouse")  # toto nehlásí chybu, pokud položka v množině není
print(f"animals = {animals}")

print(f"Is bird in animals? {"bird" in animals}")
print(f"Is mouse in animals? {"mouse" in animals}")
