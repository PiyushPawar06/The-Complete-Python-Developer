# #unorderd collection of unique objects is called sets
# # sets does not support indexing 
# my_set = {1,2,3,4,5,4}
# print(my_set) # this will give the unqiue items ie:- 4 will only print once
# my_set.add(6)
# print(my_set)

# list1 = [1,2,3,4,5,6,7,8,9,1]

# print(set(list1))
# new_set = my_set.copy()
# my_set.clear()
# print(new_set)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9}

print(set1.difference(set2))
print(set1.discard(5),set1)
# print(set1.difference_update(set2),set1) #this will modify the original  set too
print(set1.intersection(set2)) #print(set1 & set2) will give the same result
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.union(set2)) #print(set1|set2) will give the same result
