def subarray_sum(nums, target):
    # sub = {}
    # for j in range(len(nums)):
    #     for i in range(j,len(nums)):
    #         # print(i,"start")
    #         sub[i] = nums[i]
    #         if sum(sub.values()) == target:
    #             return [j, i]        
    #     sub.clear()
    # return []  
    sum_index = {
        0 : -1
    }
    current = 0
    for i, val in enumerate(nums):
        current += val

        if current - target in sum_index:
            start_index = sum_index[current-target] + 1
            return [start_index,i]
        sum_index[current] = i
     
    return []    

nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
