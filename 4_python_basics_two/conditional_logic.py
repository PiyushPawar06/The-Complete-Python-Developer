is_old = True
is_licenced = False

# truthy and falsey 
# these are used to define any values as boolean true or false
# for example if we put value of is_old = 5 and is_licenced = 'hello' is will still work

if is_licenced:
    print("You are eligible")
elif is_old:
    print("You are eligible but not licenced")
else:
    print("You are underage")