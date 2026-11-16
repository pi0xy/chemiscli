from solver import balance

equation = input("Equation: ")

try:
    print(balance(equation))
except ValueError as e:
    print("Error: ", e)