def starpattern(x):
    a = 0
    z = 0
    while z < x:
        for n in range(x-a):
            print("*", end=" ")
        a += 1 
        z += 1 
        print("\n")     

num = int(input("How large do you want the star pyramid to be?: "))
starpattern(num)