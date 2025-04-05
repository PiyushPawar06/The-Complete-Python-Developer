username = input("Enter your name: ") 
password = input("Enter your password: ")

password_length = len(password)

crypted_password = "*" * password_length 

print(f"Hello {username}, your password {crypted_password} is {password_length} characters long.")