def first_non_repeating_char(word):
    # unique = []
    # duplicate = []
    # for i in word:
    #     if i not in unique:
    #         unique.append(i)
    #     elif i not in duplicate:
    #         duplicate.append(i)
    # for i in unique:
    #     if i not in duplicate:
    #         return i      
    frequency = {}
    for char in word:
        frequency[char] = frequency.get(char, 0) + 1
    for i, val in frequency.items(): 
        if val == 1:
            return i   
    

print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""