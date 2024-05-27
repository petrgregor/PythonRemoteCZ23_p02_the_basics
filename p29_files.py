# Opening a File - method 1
f = open('file.txt')  # otevřu soubor
# pracuji se souborem
read_next = True
while read_next:
    line = f.readline()
    if not line:
        read_next = False
    print(line, end="")
f.close()  # zavřu soubor

print()

# Opening a file - method 2
with open('file.txt') as f:
    lines = f.readlines()  # seznam obsahující jednotlivé řádky
    print(lines)

    for line in lines:
        print(line, end="")
    # automaticky se soubor uzavře, pokud vyskočíme z tohoto bloku

print()
# Reading from a file - method 3
with open('file.txt') as f:
    for line in f:
        print(line, end="")

print()
# Writing to a file
with open('output.txt', 'w') as f_out:
    for i in range(10):
        f_out.write(f"this is line number {i} \n")

with open('output2.txt', 'w') as f_out:
    with open('file.txt') as f_in:
        i = 1
        for line in f_in:
            f_out.write(f"{i}: {line}")
            i += 1
    print("All lines are copied!")

print("OK")
