def exponent(x, y):
     result = x ** y
     return result

def explain(x, y):
    print("e.g.", end=" ")
    for n in range(1,y):
        print(x,"*", end=" ")
    print(x,"=", exponent(x,y)) 

base = int(input("Please enter the base number: "))
exp = int(input("Please enter the exponent: "))
#print("\n")
#print(base,"raised to the power of",exp,"\b:",exponent(base,exp))
print(explain(base,exp))      