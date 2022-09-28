#establish given lists for comparison
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

#define comparison function with user input for string name
def comparelist(x):
    if x[0] == x[-1]:
        print("\nGiven list: ",x)
        result = bool(x[0] == x[-1])
        print("\nThe result is ",result)
    else:
        print("\nGiven list: ",x)
        result = bool(x[0] == x[-1])
        print("\nThe result is ",result)
        
#ask for user input and use the comparison function on that string name
#userinput = input("What is the name is the string you want to compare?: ")
comparelist(numbers_x)
comparelist(numbers_y)