def idnum(x):
    z = -1
    for y in range(len(x)):
        if x[y] == x[z]:
            z -= 1
            if abs(z) == len(x):
                print("The number is a palindrone.")
        else:
            print("The number is not a palindrome.")
            break
        
usernum = input("Give a number to determine if it's a palindrome: ")
idnum(usernum)