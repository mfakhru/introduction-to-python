# ASSIGNMENT OPERATOR
""" used to (re)bind names to values and to modify
    atributes or items of mutable objects.

    in short, it works as follows (simple assignment):
    1)  an expression on the right hand side is evaluated,
        the corresponding object is created/obtained
    2) a name on the left hand side is assigned, or bound, to the r.h.s object
"""

## a single object can have several names bound to it
a = [1, 2, 3]
b = a
print(a)
print(b)
print(a is b)
b[1] = 'hi!'
print(a)

print('\n========')
## to change a list in place, use indexing/slice
a = [1, 2, 3]
print(a)
# create another object
a = ['a', 'b', 'c']
print(a)
print(id(a))
# modifies object in place
a[:] = [1, 2, 3]
print(a, id(a)) # same id

"""
    the key concept here is mutable vs immutable
    >> mutable object can be changed in places
    >> immutable object cannot be modified once created
"""

