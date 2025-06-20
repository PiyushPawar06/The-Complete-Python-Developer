# i = 0
# while i<10 :
#     print(i)
#     i +=1
# # print(i)
# # while loop is used when we want to run the loop for a time period where the condition remains the same
# while True:
#     a = input("What up? : ")
#     if a == "bye":
#         break #this is used to break the while loop irrespective of the condition
# print(a)

# # continue is a keyword used to make the loop continue irrespective of anything

my_list = [1,2,3,4,5,6]
i = 0
while i <len(my_list):
    i += 1
    continue
    print(i) # here the loop will continue and not reach this line as the keyword contiune is used before this print statement
pass # used rarely it does nothing but pass to the next line . it can be used as a placeholder 

# exercise

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for i in picture:
    for a in i:
        if a == 1:
            print("*", end = "")
        else:
            print(" ", end = "")
    print('')