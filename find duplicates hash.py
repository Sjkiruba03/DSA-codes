# WRITE FIND_DUPLICATES FUNCTION HERE #
#                                     #
#                                     #
#                                     #
#                                     #
#######################################
def find_duplicates(lists):
    num_counts = {}
    for num in lists:
        num_counts[num] = num_counts.get(num, 0) + 1
        
    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)
 
    return duplicates    
    # uniqueList = []
    # duplicateList = []
 
    # for i in lists:
    #     if i not in uniqueList:
    #         uniqueList.append(i)
    #     elif i not in duplicateList:
    #         duplicateList.append(i)             
      
    # return duplicateList


print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

