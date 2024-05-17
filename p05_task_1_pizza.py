"""
Task 1: Which pizza has the best price/quantity ratio?

Write a program that will compare the area/price ratio between two pizzas.
In order to calculate the area of a circle P at a given radius r - use this formula - Formula.

Find a restaurant in your area, enter the appropriate data and answer the question asked in the recommendation.

Important
You can use the math standard library to get the exact value of pi, but it is not required.

Hint
It's worth creating a function that computes the whole so that it doesn't repeat itself twice.
"""

PI = 3.14159
"""
r1 = 16  # poloměr
r2 = 18
price1 = 150
price2 = 196
"""

print("Welcome to our pizza solver.")
r1 = float(input("Enter radius of pizza 1: "))
price1 = float(input("Enter price of pizza 1: "))
r2 = float(input("Enter radius of pizza 2: "))
price2 = float(input("Enter price of pizza 2: "))

print(f"Pizza 1 with radius {r1} cm and price {price1} CZK has area/price ratio {(PI * (r1 ** 2)) / price1:.5f} cm2/CZK")
print(f"Pizza 2 with radius {r2} cm and price {price2} CZK has area/price ratio {(PI * (r2 ** 2)) / price2:.5f} cm2/CZK")
print(f"{((PI * (r1 ** 2)) / price1) > ((PI * (r2 ** 2)) / price2)}")
