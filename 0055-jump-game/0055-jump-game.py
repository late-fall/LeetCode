class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        def checklast(nums):
            idx = len(nums) - 2
            step = 1

            while idx >= 0:
                if nums[idx] >= step:
                    return 1
                idx -= 1
                step += 1
                
            return 0
        
        def checkzero(nums):
            idx = len(nums) - 2
            step = 1

            while idx >= 0:
                if nums[idx] > step:
                    return 1
                idx -= 1
                step += 1
                
            return 0
        
        res = 0
        total = 0 
        
        for i, n in enumerate(nums):
            if i == (len(nums) - 1):
                res += checklast(nums[:i+1])
                total += 1
            elif n == 0:
                res += checkzero(nums[:i+1])
                total += 1
        return res == total
            