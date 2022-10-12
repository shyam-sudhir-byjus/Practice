from curses.ascii import isdigit
from sympy import symbols, Eq, solveset
from simple import find_number
equation = "x**2-128=0"

if equation[0] == 'x':
    var = symbols('x')
elif equation[0] == 'y':
    var = symbols('y')
elif equation[0].isdigit():
    number_left = float(equation[0])


number = find_number(equation)

sols = solveset(var**2 - float(number), var)
print(sols)
