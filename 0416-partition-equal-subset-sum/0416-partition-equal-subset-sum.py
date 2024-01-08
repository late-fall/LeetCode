class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        
        def canSum(target, num, i, mem={}):
            if (i, target) in mem:
                return mem[(i,target)]
            if nums[i] == target:
                return True
            if target < 0 or i == len(nums)-1:
                return False
            res = canSum(target, nums, i + 1, mem) or canSum(target - nums[i], nums, i+1, mem)
            mem[(i,target)] = res
            return res
        
        return canSum(target, nums, 0, {})