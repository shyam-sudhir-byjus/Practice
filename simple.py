from sympy import symbols, Eq, solveset


def find_number(equation):

    def find_number_zero_right(equation):
        equation_left = equation.split('=')
        return equation_left[0]

    def check_whether_0(equation):
        if equation[-1] == '0' and equation[-2] == '=':
            return True
        return False

    if check_whether_0(equation):
        equation = find_number_zero_right(equation)
        if '**2' in equation:
            number = equation.split("**2")[1]
        elif '^2' in equation:
            number = equation.split("^")[1]
        else:
            number = equation.split("x2")[1]
        if (number[0] == '-'):
            return float(number[1:])
        else:
            return -float(number[1:])
    else:
        number = equation.split('=')[1]
        return float(number)


equation = "5x2 - 450=0"
equation = equation.replace(" ", "")

if 'x' in equation:
    var = symbols('x')
    variable = 'x'
    x_index = equation.index('x')
    if equation[x_index+1].isdigit() and equation[x_index+1] != '2':
        print('Error')
    elif equation[x_index+2].isdigit() and equation[x_index+2] != '2':
        print('Error')
    elif '**' in equation:
        print('yes')
        eq_right_num = equation.split('**')[1][0]
        if eq_right_num != '2':
            print('Error')
    elif '^' in equation:
        eq_right_num = equation.split('^')[1][0]
        if eq_right_num != '2':
            print('Error')

    if equation[0] == 'x':
        number_left = float(1)
    elif equation[0].isdigit():
        coeff = equation.split('x')[0]
        number_left = float(coeff)
else:
    var = symbols('y')
    variable = 'y'
    if equation[0] == 'y':
        number_left = float(1)
    elif equation[0].isdigit():
        coeff = equation.split('y')[0]
        number_left = float(coeff)

number = find_number(equation)
print(number/number_left)
sols = solveset(var**2 - number, var)
print(sols)
