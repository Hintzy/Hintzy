def idnum(x):
    z = -1
    temp = str()
    for y in range(len(x)):
        temp[y] = x[z]
        z -= 1
        if temp == x:
            print ("The number is a palindrome.")
        else:
            print("The number is not a palindrome.")
            
usernum = input("Give a number to determine if it's a palindrome: ")
idnum(usernum)