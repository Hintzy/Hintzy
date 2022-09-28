number1 = int(input("Number 1 equals:"))
number2 = int(input("Number 2 equals:"))

def calc(number1, number2):
    number3 = number1 * number2
    number4 = number1 + number2
    if number3 <= 1000:
        print("The result is "+ str(number3) +".")
    else:
        print("The result is "+ str(number4) +".")

calc(number1,number2)