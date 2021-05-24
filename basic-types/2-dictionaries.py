# DICTIONARY
# basically an efficient table that maps keys to values
# It is an unordered container

tel = {'emmanuelle': 5752, 'sebastian': 5578}
tel['francis']=5915
print(tel)

print(tel['sebastian'])
print(tel.keys())
print(tel.values())
print('francis' in tel)

# it can be used to conveniently store
d = {'a': 1, 'b':2, 3:'hello'}
print(d)