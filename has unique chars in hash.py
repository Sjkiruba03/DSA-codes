def has_unique_chars(word):
    # dict1 = {}                Method 1
    # for i in word:
    #     can = dict1.get(i,0)+1
    #     dict1[i] = can   
    # for i in dict1.values():
    #     if i > 1:
    #         return False
    # return True

    # Method 2

    new_set = set()
    for i in word:
        if i in new_set:
            return False
        new_set.add(i)
    return True    

    # list1 = []                   Method 3
    # for i in word:
    #     list1.append(i)
    # new_list = list(set(list1))        
    # if sorted(list1) == sorted(new_list):
    #     return True
    # return False   


print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""