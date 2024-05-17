import sys

print("Welcome")
print(f"All arguments: {sys.argv}")
print(f"Program name: {sys.argv[0]}")
print(f"First argument: {sys.argv[1]}")
print(f"Second argument: {sys.argv[2]}")

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

print(f"Arguments: {arg1}, {arg2}, {arg3}")
