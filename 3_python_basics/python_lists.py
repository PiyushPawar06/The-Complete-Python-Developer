# list is the a collection of datatypes that might be similar or different and is  defined in []
# its mutable 

li = [1,2,3,4]
li2 = ['a','b','c']
li3 = [1,2,'a',True]

items = ['butter', 'chicken', 'vegetables','fruits','milk']
print(items[0])

# list slicing
print(items[0::2])
new_items = items[:] # this will give a copy of the list into the new_items list
new_items[0] = 'Ghee' # lists are muteable , it makes a copy of the list while sciling
print(new_items)
print(items)

# matrix

matrix = [
    [1,2,3],
    [2,4,6],
    [5,6,8]
    ]

print(matrix[0][1])