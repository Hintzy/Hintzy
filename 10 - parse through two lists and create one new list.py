def merge_list(list1, list2):
    list3 = []
    
    for x in list1:
        if x%2 != 0:
            list3.append(x)

    for x in list2:
        if x%2 == 0:
            list3.append(x)
    
    return list3

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print("Resulting list: ", merge_list(list1, list2))