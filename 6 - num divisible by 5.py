def div5(x):
    print("The numbers is the list divisible by 5 are: ") 
    for y in range(len(x)):
        mod = int(x[y]) % 5
        if mod == 0:
            print(x[y])
            y += 1
        else:
            y += 1
            
exlist = [10, 20, 33, 46, 55, 60, 72, 73, 74, 75, 90, 95, 100, 101]
div5(exlist)