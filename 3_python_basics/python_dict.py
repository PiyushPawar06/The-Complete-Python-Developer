dictionary = {
    'a': 1,
    'b': 2
}

print(dictionary['a'])
print(dictionary) # dictionary is a group of unordered key value pairs

dictionary_1 = {
    'a': 1,
    'b': 2,
    'c':[1,2,3]
}

print(dictionary_1['c'][2])

my_list = [
    {
    'a': 1,
    'b': 2,
    'c':[1,2,3]  
    },
    {
    'a': 1,
    'b': 2,
    'c':[4,5,6] 
    }
]

print(my_list[1]['c'][1])
# in dictionary the key should be immutable meaning it should not change 
# key has to  be unique

random_dict = [
    {
        12 : [1,2],
        True : "Hello"
    },
    {
        'jib' : True
    }
]
print(random_dict[1]['jib'])

butter = {
    'masala': 1,
    'chicken' : 500
}
print(butter.get('get', 'all')) # this will set an default value in the dictionary 
print('masala' in butter)
print('chicken' in butter.keys())
print(500 in butter.values())
print(butter.items())   
butter.update({'masala':2})
print(butter)

#another way to create a dictionary

user = dict(name="Piyush")
print(user)
user2 = user.copy()
user.clear()
print(user)
print(user2)
