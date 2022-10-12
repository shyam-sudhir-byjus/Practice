import math
import sympy
from sympy import symbols, factor, expand, diff, integrate, limit, oo, Eq, solve, dsolve, Function, Matrix

'''
    x = symbols('x')
    y = symbols('y')
    
    expression = 2*x + y
    print(expression - x)  # x + y
    
    FACTORING AND EXPANDING
    
    expr = 2 * x + 2*y
    print(factor(expr))  # 2*(x+y)
    expr1 = x**2 * (x + y)
    print(expand(expr1)) # x**3 + x**2*y
    
    DIFFERENTIATION
    
    formula = x**2
    print(diff(formula)) # 2*x
    print(diff(sympy.exp(x)))
    print(diff(sympy.sin(x) + sympy.cos(x)))
    
    INTEGRATION(EQN, (VAR, LOWER, HIGHER))

    print(integrate(2**x, (x, 0, 10)))
    print(integrate(sympy.sin(x**2), (x, -oo, oo)))  # oo is infinity

    LIMIT(EQ, VARIABLE, LIMIT)
    
    print(limit(50/x, x, 0))  # oo
    print(limit(sympy.sin(x)/x, x, 0))  # 1
    
    SOLVE(EQUAL(EQUATION, VAR))

    print(solve(Eq(x**2, y), x)) # x = [-sqrt(y),sqrt(y)]

    DIFFERENTIAL EQUATIONS
    
    t = symbols('t')
    y = Function('y')
    # y(t)'' - y(t) = e^t
    print(dsolve(Eq(y(t).diff(t, t) - y(t), sympy.exp(t)), y(t))) 
    # OUPUT WILL BE => Eq(y(t), C2*exp(-t) + (C1 + t/2)*exp(t))
    
    MATRIX EIGEN VALUES
    
    print(Matrix([[1, 2], [2, 2]]).eigenvals()) 
    # OUTPUT => {3/2 - sqrt(17)/2: 1, 3/2 + sqrt(17)/2: 1}
    
'''
