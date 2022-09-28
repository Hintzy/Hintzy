userstring = input("Please enter a string of text: ")
print("The original text string is: ", userstring)
print(type(userstring))

for i in range(0,len(userstring),2):
    print("index[",i,"]", userstring[i])