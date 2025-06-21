my_list = ['a','b','c','b','d','m','n','n']

dups = []
for items in my_list:
    if my_list.count(items) > 1:
        if items not in dups:
            dups.append(items)
print(dups)