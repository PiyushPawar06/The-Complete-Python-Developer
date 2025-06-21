
#this is a funtion. it is a powerfull tool used in python that helps us increase code reusablity and we can make our on fuctions if needed.
# parameters are used in functions . these parameters are variables that we write in the () of the function.
def hello_guys(name, emoji):
    print(f"hiiiii! {name} {emoji}")

#when we give those parameters while calling the function (like below) we call them arguments
hello_guys("Piyush" , ":)") # this is the positinal argument as we ahave to give the arguments in the same squence as the parameters ae given above in the function.

hello_guys(emoji=":/",name="Aryan") # these are the keyword arguments because we provide the key and its value together. so it considers the given value irrespective of its position.
# this is usually considered as bad practice as parameters sqeunce are to be followed.

def yello(name = "Vishwa", emoji = "(-.-)"): # this is known as default parameter. it is set when we want to display something as default if arguments are not passed by the user.
    print(f"yello {name} {emoji}")

yello()
yello("Tigu",";)")

# return is  a keyword used in function a lot as it returns the expression that a function performs. if the reutrn is not provided then function returns None.

def addition(num1 , num2):
    return num1 + num2

print(addition(6 , 2))

def sum(num1 , num2):
    def another_func(n1 , n2):
        return n1 + n2
    return another_func(num1 , num2)
total = sum(10,20)
print(total)

# a funtion should perfrom one clean expression 
# a funtion should return something.
# a return statement exits the function.