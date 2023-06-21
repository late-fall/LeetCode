class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        t = len(nums)
        counts = {0:0, 1:0, 2:0}
        
        for i, n in enumerate(nums):
            if n == 0:
                counts[0] += 1
            elif n == 1:
                counts[1] += 1
            else:
                counts[2] += 1
        
        zero = counts[0]
        one = counts[1]
        two = counts[2]
        
        for i in range(zero):
            nums[i] = 0
        for i in range(zero, zero + one):
            nums[i] = 1
        for i in range(zero + one , zero+ one + two):
            nums[i] = 2
        
            # if n == 0:
            #     nums[i], nums[counts[0]] = nums[counts[0]], nums[i]
            #     counts[0] += 1
            # elif n == 2:
            #     nums[i], nums[t - 1 - counts[2]] = nums[t - 1 - counts[2]], nums[i]
            #     counts[2] += 1
            # else:
            #     nums[i], nums[counts[0] + counts[1] + 1] = nums[counts[0] + counts[1] + 1], nums[i]
            #     counts[1] += 1
            # print(nums)
        
        return nums