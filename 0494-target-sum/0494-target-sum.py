class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def backtrack(idx, subtarget):
            if idx == len(nums):
                return 1 if subtarget == target else 0
            
            if (idx+1,subtarget+nums[idx]) not in cache:
                cache[(idx+1, subtarget+nums[idx])] = backtrack(idx+1, subtarget + nums[idx])
                
            if (idx+1,subtarget-nums[idx]) not in cache:
                cache[(idx+1, subtarget-nums[idx])] = backtrack(idx+1, subtarget - nums[idx])
            
            return cache[(idx+1, subtarget+nums[idx])] + cache[(idx+1, subtarget-nums[idx])]
        
        return backtrack(0,0)
            