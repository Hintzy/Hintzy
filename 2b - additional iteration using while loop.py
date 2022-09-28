#takes a starting number, iteration size, and amount of iterations from the user and sets that to integer values
num1 = int(input("Please indicate a starting number: "))
itersize1 = int(input("Please indicate the size of each iteration: "))
itermax1 = int(input("Please indicate amount of iterations: "))

#defining function
def iterate(num,itersize,itermax):
    iter = 0
    prev = 0
    while iter < itermax:
        sum1 = num + prev
        print("Current Number is", num, "Previous Number is", prev, "Sum is:", sum1)
        prev = num
        num += itersize
        iter += 1

iterate(num1,itersize1,itermax1)