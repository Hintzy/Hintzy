def extractandreverse(num):
    
    new_num = 0
    num_int = int(num)
    
    print("The reverse of the provided number is:", end=" ")
    
    for x in range(len(num)):
        last_digit = num_int % 10
        num_int = num_int // 10
        print(last_digit, end=" ")

num = input("Please provide a number to reverse: ")
extractandreverse(num)