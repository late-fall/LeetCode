class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_dif = -1
        
        i = 0
        j = 1
        
        while j < len(nums):
            if nums[i] < nums[j]:
                max_dif = max(max_dif, nums[j] - nums[i])
            else:
                i = j
            j += 1
            
        return max_dif