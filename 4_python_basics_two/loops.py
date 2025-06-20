for item in [1,2,3,4,5,6]:
    # print(item) # as it is intended it falls under the loop and will be executing till the loop stops
    for x in ["a","b","c"]:
        print(x, item)
print("Hi") # this is outside the loop so it will only print one

# iterables are those items that can be checked one by one in a colection.
# iterables exammples are list, set, tuples, dict., string.

user = {
    'name': "Piyush",
    'age': 24,
    'can_swim':False
}

for a in user: # also gives the keys from the dict.
    print(a)

for a in user.items(): # gives the key pair values from the dict.
    print(a)

for a in user.values(): # gives the values from the dict.
    print(a)

for key,value in user.items(): # gives the keys and values with brackets from the dict.
    print(key,value)

my_list = [1,2,3,4,5,6,7,8,9,10]
total = 0
for item in my_list:
    total += item
print(total)

range(0,10) # this is a object used to iterate from 0 to 100 and is commonly used in loops
for numbers in range(1,10,2): # here you can also write only the number till which you want to iterate and also the last number is alway left as the iteration starts from the index of 0. the 2 in the range is the step fuction that jumps to the next number, as step is 2 here it will jump from 1 to 3.
    print(numbers)

for i,char in enumerate([1,2,3,4,5,6]): # helps you know the index of the iterables.here i represents the index and can or cannot be used.
    print(i,char)

for a,num in enumerate(list(range(10))):
    print(a,num)
    if num == 2:
        print(f"index is {a}")