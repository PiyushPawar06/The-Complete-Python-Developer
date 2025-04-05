# a string is a datatype used to tell the value that is a letter or a sentence 

name = 'Piyush' # here the '' is used to define the word Piyush which is a string
password = "123" # here 123 can be written as a string using '' or " " quotes 
doc_string = ''' hello world this is a long string it can be multiple lines. it is also called docstring. triple quotes are used to write this docstrings'''
print(doc_string)

# string concatenation is were we join to strings using +
login = name + password
print(login)
# but this will not give any spaces in between
# string concatenation only works with strings and not another datatype 

# type conversion 
print(type(str(12232))) # this will give the type as string as we use str keyword and have converted the number 12232 into a string 

# Escape Squences
# it is done by using the \ and is used so that we can write the string without any error
message = "It's a \"beuatiful \"day" # here whatever is after the \ is considered as a string
print(message) 
a = "\t wow" # this will give me a tab before the string as I have mentioned \t(t stands for tab)
print(a) # \n is for new line

# formatted strings are those strings were we add the varibales into {} and write the string easily 
name = "Aryan"
age = 23
print(f"hello {name} you're {age} years old.") # f is used to format the string with the varibales.

# String indexes 
numbers = "1234556789"
print(numbers[0]) #this will give the index 0 value which is 1 and in computer science the numbers for index start from 0
# the index should defining is done in [] and you can add start and stop and step to this opreation.
print(numbers[0:8:2]) # here the index will start at 0 till 8 and step by 2 also as soon as it gets to  8 it will stop and also exclude the value at index 8 
# the -ve index will start the indexing of a string from the end of the string 
print(numbers[-1])
print(numbers[::-1]) # this will give the reverse format of a string

# strings are immutable , meaning you cant chage the values of that string(index wise), the entire string can be changed but not index wise 