#define function for taking two inputs to create a multiplication table
def createmulttable(n1,n2):
    for x in range(1,n1+1):
        #cycle through the values for each number iteration
        for y in range(1,n2+1):
            printnum = x*y
            print('{:<3} and {:>3}'.format(printnum,printnum), end=" ")
        print("\n")
        
#take two user based integer inputs to create a multiplication from
num1 = int(input("Please give the first parameter for the multiplication table: "))
num2 = int(input("Please give the second parameter for the multiplication table: "))
createmulttable(num1,num2)