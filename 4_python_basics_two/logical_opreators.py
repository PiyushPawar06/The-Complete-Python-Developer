# these are the opreators used to perform logical operations
# >
# < 
# ==
# !=
# >=
# <=
# and or not 

# Exercise 

is_magician = True
is_expert = False

if is_magician and is_expert:
    print("You're a master magician")
elif is_magician and not is_expert:
    print("you're getting there")
elif not is_magician:
    print("you need magical powers")
