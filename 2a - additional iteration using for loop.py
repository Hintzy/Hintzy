#takes a number from the user
num1 = int(input("Please indicate a starting number: "))
itermax1 = int(input("Please indicate amount of iterations: "))

def iterate(num):
    prev = 0
    for iter in range(10):
        sum1 = num + prev
        print("Current Number is", num, "Previous Number is", prev, "Sum is:", sum1)
        prev = num
        num += 1
        iter += 1

iterate(num1)