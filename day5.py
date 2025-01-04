usr_inpt= input("Enter the string: \t")
print("Printing the characterers at the even position: \t")
for i in range(0, len(usr_inpt), 2):
    print(usr_inpt[i], end="")