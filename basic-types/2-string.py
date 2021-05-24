## STRING

# different string syntaxes (simple, double, or triple quotes)
s1 = 'Hellow how are you?'
s2 = "Hi, what's up"
s3 = '''Hello,
        how are you'''
s4 = """Hello,
        how are you"""
# print(s3)

"""
        if 'Hi, what's up?'
        it's error, you must use ".."
        or use backslash ex: 'what\'s up?'

        Other uses of the blackslash
        \n -> newline character
        \t -> tab character

"""

# Indexing
print('===INDEXING===')
a = 'hello'
print(a[0],a[1],a[-1])

# Slicing
a = 'hello, world!'
print(a[3:6]) # 3rd to 6th (excluded)
# syntax: a[start:stop:step]
print(a[2:10:2])
# every three characters, from beginning to end
print(a[::3])

# create new string
repl= a.replace('l', 'z', 1)
print(repl)

repl= a.replace('l', 'z')
print(repl)

print('\n===STRING FORMATING===')
# with more values use tuple after %
print('An integer: %i; a float = %f; another string: %s' % (1, 0.1, 'string'))
i = 102
# no need for tuples with just one value after %
filename = 'processing_of_dataset_%d.txt' %i
print(filename)