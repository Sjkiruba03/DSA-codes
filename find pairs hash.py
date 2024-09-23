def find_pairs(arr1, arr2, target):
    # output = []
    # new_set = set(arr1)
    # for i in arr1:
    #     if target - i in arr2:
    #         output.append((i , target-i))
            
    # return output
        
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs





    # output = []
    # for i in arr1:
    #     for j in arr2:
    #         if i+j == target:
    #             output.append((i,j))
                

    # return output



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""