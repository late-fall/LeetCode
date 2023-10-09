class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def backtrack(idx, subtarget):
            if idx == len(nums):
                return 1 if subtarget == target else 0
            
            if (idx+1,subtarget+nums[idx]) in cache:
                plus = cache[(idx+1, subtarget+nums[idx])]
            else:
                plus = cache[(idx+1, subtarget+nums[idx])] = backtrack(idx+1, subtarget + nums[idx])
                
            if (idx+1,subtarget-nums[idx]) in cache:
                minus = cache[(idx+1, subtarget-nums[idx])]
            else:
                minus = cache[(idx+1, subtarget-nums[idx])] = backtrack(idx+1, subtarget - nums[idx])
            
            return plus + minus
        
        return backtrack(0,0)
            