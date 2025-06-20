# this operator makes the code even simpler , basically a one liner.

is_friend = True

can_messege = "Allowed" if is_friend else "not allowed"
print(can_messege)

# Short Circuting 
# the python interpretor does this when the any operation isnt neccessary to be performed and seems like extra work

user1 = True
user2 = True

if user1 or user2 :
    print("Both are classmates")

# above if one of this is true then the python interpretor doesnt perform the remaining part.