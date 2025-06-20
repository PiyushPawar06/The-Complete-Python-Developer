user_input = str(input("Provide a string:"))
new_set = set()
new_str = ""
for dup in user_input:
    if dup not in new_set:
        new_set.add(dup)
        new_str +=dup

print(new_str)


    

