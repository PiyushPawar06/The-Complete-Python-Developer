my_list = ['a','b','c','b','d','m','n','n']

dups = []
for items in my_list:
    if my_list.count(items) > 1:
        if items not in dups:
            dups.append(items)
print(dups)

# functions exercise 

def highest_even(my_list):
    even_num = []
    for value in my_list:
        if value % 2 == 0 :
            even_num.append(value)
    return max(even_num)

print(highest_even([1,2,3,4,5,69,11,12,44,100]))
   