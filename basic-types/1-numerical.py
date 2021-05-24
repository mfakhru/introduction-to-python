## NUMERICAL TYPES

"""
    Python supports the following numerical,
    sclar types:
    1) Integer
    2) Float
    3) Complex
    4) Booleans
"""

# Integer
print("===INTEGER===")
a = 4
print(a, "is", type(a))

# Floats
print("\n===FLOAT===")
b = 9.9
print(b, "is", type(b))

# Complex
print("\n===COMPLEX===")
comp = 4.2 + 9.1j
print("4.2 + 9.1j")
print("real= ", comp.real, "imag= ", comp.imag)
print(type(comp))

# Booleans
print("\n===BOOLEAN===")
test = (3 > 4)
print("3 > 4 = ", test, "is", type(test))

"""
    A python shell can therefore replace your
    pocket calculator, with basic arithmetic
    operations:
    1) +
    2) -
    3) *
    4) /
    5) % (modulo)
"""
print("\n===ARITHMETIC===")
# example
ex1 = a + b
print(a, "+", b, "=", ex1)

ex2 = a * b
print(a, "*", b, "=", ex2)

# type conversion
print("\n===CASTING===")
x = float(a)
print(x, type(x))

# example2
y = 3 / 2
print(y)

# if you explicitly want integer division user "//"
z = 3.0 // 2
print(z)
