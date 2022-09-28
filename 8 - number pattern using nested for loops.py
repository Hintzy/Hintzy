def pattern(x):
    for y in range(x):
        for z in range(y+1):
            print(y+1, end=" ")
        print("\n")

userinput = int(input("How high do you want the pattern to go?: "))
pattern(userinput)