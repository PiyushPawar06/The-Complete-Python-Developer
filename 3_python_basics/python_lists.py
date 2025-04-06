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


# List methods 
# methods modifies the list ie:- inplace is true. a new list is not made.

basket = [1,2,3,4,5]

# adding  
basket.append(6) # this will add 6 at the end of the list 
basket.insert(0, 0)
new_basket  = basket
print(basket,new_basket)

# removing

basket.pop(0) # we give the index  
basket.remove(5) # we give the vlaue
# basket.clear() # will clear the list
new_basket  = basket
print(basket,new_basket)

# other methods
basket1 = ['a','b','c','a','d','e']
new_basket  = basket
print(basket1.index('b')) # will give the index number of the value which is 'b' here 

# use of keywords in lists
basket1.sort() # will sort the list 
print(sorted(basket1)) # this funtion will make a copy of the list without changing the list
print(basket1)
print(basket1.count('a')) # will count the number of occurance of a
print( 'a' in basket1)
print('i' in 'hello I am a Student')
basket1.reverse() # will reverse the list accordingly
print(basket1)

print(list(range(100))) # will make a list from 0 to 99

sentance  = " ".join(['a', 'for', 'apple']) 
print(sentance)

#list unpacking

a,b,c, *other = [1,2,3,4,5,6,7,8,9]

print(a,b,c)
print(other)