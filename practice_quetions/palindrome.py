User_input = str(input("Please provide a number or a word: "))
palindrome = User_input[::-1]

if palindrome == User_input:
    print("Given input is palindrome")
else:
    print("Its not a palindrome")