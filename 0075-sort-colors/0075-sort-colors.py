class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
#         t = len(nums)
#         counts = {0:0, 1:0, 2:0}
        
#         for i, n in enumerate(nums):
#             if n == 0:
#                 counts[0] += 1
#             elif n == 1:
#                 counts[1] += 1
#             else:
#                 counts[2] += 1
        
#         zero = counts[0]
#         one = counts[1]
#         two = counts[2]
        
#         for i in range(zero):
#             nums[i] = 0
#         for i in range(zero, zero + one):
#             nums[i] = 1
#         for i in range(zero + one , zero+ one + two):
#             nums[i] = 2
        
#             # if n == 0:
#             #     nums[i], nums[counts[0]] = nums[counts[0]], nums[i]
#             #     counts[0] += 1
#             # elif n == 2:
#             #     nums[i], nums[t - 1 - counts[2]] = nums[t - 1 - counts[2]], nums[i]
#             #     counts[2] += 1
#             # else:
#             #     nums[i], nums[counts[0] + counts[1] + 1] = nums[counts[0] + counts[1] + 1], nums[i]
#             #     counts[1] += 1
#             # print(nums)
        
#         return nums
    
    # NEET code solution
    # bucket sort O(n), since we only have 3 values. 
    
    # count how many values are present.
    # use hashmap, extra size of 3 hashmap
    # quick sort - partitioning
    
        l, r = 0, len(nums) - 1
        i = 0 

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1 # to cancel i += 1
            i += 1