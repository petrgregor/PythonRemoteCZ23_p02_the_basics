"""
TODO: Task 3: Dancing parabolas

Write a program that will calculate the zeros of the given square function.
For this purpose, you can use the formulas presented here.

Note
We assume movement only in the space of real numbers, complex solutions are not required.
"""

# řešíme kořeny kvadratické rovnice ve tvaru ax^2 + bx + c = 0
# https://www.umimematiku.cz/cviceni-reseni-kvadraticke-rovnice

import sys
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

"""
print("Welcome to square function solver.")
print("Square function has format ax^2 + bx + c - 0.")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
"""

print(f"Your square function is: {a}x^2 + {b}x + {c} = 0")

d = b**2 - 4*a*c
print(f"d = {d}")

x1 = (-1*b - d ** (1/2)) / (2*a)
x2 = (-1*b + d ** (1/2)) / (2*a)

print(f"Kořeny jsou: x1 = {x1:.3f}, x2 = {x2:.3f}.")
