#take input string and amount of characters to remove from beginning
userstring = input("Please enter a text string: ")
delnum = int(input("Indicate how many characters to remove from the beginning of the string: "))

#ensure amount of deleted characters is not longer than the text string
def lencheck(x,y):
    if x > y:
        x = int(input("\nCannot remove more characters than the length of the original string.\nHow many characters would you like to remove from the beginning of the string? "))
        lencheck(x,y)
lencheck(delnum,len(userstring))

#remove the specified amount of characters from the provided text string
def chardel(x):
    newstring = userstring[x:]
    return newstring

print("\nThe modified string is:", chardel(delnum))