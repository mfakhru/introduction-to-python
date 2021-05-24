## CONTAINERS
# python provides many effcient type of containers
# in which collections of objects can be stored

# LIST
print("\n===LIST===")
colors = ['red', 'blue', 'green', 'black', 'white']
print(colors, "is", type(colors))
print(colors[2]) # accessing individual objects
print(colors[-1]) # from the ends
print(colors[-2])

# indexing start at 0, not at 1
print(colors[2:4])

"""
    colors[start:stop] contains the elements with indices i
    such as start <=i < stop (i ranging from start to stop -1)
    Therefore, (stop - start) elements

    slicing syntax: colors(start:stop:stride)
"""
# let's see!
print("\n===Slicing Syntax===")
print(colors[3:]) # slice 3 in front
print(colors[:3]) 
print(colors[::2]) # 0 : 2 : 4

# list are mutable objects and can be modified
colors[0] = 'yellow'
print(colors)
colors[2:4] = ['gray', 'purple']
print(colors)

# the elements of a list may have different types
colors = [3, -200, 'hello']
print(colors)
print(colors[1], colors[2])

print("\n===ADD AND REMOVE ELEMENTS===")
colors = ['red', 'blue', 'green', 'black', 'white']
print(colors)
# add
colors.append('pink')
print(colors)
# remove
colors.pop() # remove and return the last items
print(colors)
# extend
colors.extend(['pink', 'purple']) # extend colors, in-place
print(colors)
print(colors[:-2])

print("\n===REVERSE===")
rcolors = colors[::-1]
print(rcolors)
rcolors2 = list(colors) # new object that is a copy of colors in a different memory area
print(rcolors2)
rcolors2.reverse() # in-place; reversing rcolors2 does not affect colors
print(rcolors2)

print("\n===CONCATENATE AND REPEATE LISTs===")
conlist = colors + rcolors
print(conlist)
rcolorscon = rcolors * 2
print(rcolorscon)

print("\n===SORT===")
print(sorted(rcolors)) # new object
print(rcolors)
rcolors.sort()
print(rcolors)

"""
    The notation rcolors.method() (e.g. rcolors.append(3) and colors.pop()) 
    is our first example of object-oriented programming (OOP). Being a list,
    the object rcolors owns the method function that is called using the notation .. 
    No further knowledge of OOP than understanding the notation . 
    is necessary for going through this tutorial.

    rcolors.append
    rcolors.count
    rcolors.extend
    rcolors.index
    rcolors.insert
    rcolors.pop
    rcolors.remove
    rcolors.reverse
    rcolors.sort
"""

