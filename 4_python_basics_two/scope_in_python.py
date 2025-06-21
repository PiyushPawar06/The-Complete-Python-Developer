# scope tells us what variables we have access to 
# if a vairable in outside the funtion i has a global scope

total =100 # this has a global scope and can be called throughout the function.

# rules for scope
# 1. start with local 
# 2. parent local - if nested function does not have scope then scope shifts to parent function.
# 3. global - third priority 
# 4. built in python function
# above is the priority list of variable and there scopes

def count():
    global total # here global keyword is used to acces the total variable which is outside the function. 
    total += 1
    return total

print(count())

# rather then using global keyword to access the variable which is outside the funtion simply use the dependency injection where you add that global variable as aparameter in a function.

b = 12
def slove(b):
    b += 1
    return b
print(slove(slove(b)))

# nonlocal keyword is used to access the variable of parent function and override it as its own variable where you can change it to a newer value.