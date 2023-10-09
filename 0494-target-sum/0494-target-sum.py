class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def backtrack(idx, subtarget):
            if idx == len(nums):
                if subtarget == target:
                    return 1
                return 0
            
            if (idx+1,subtarget+nums[idx]) not in cache:
                plus = backtrack(idx+1, subtarget + nums[idx])
                cache[(idx+1, subtarget+nums[idx])] = plus
            else:
                plus = cache[(idx+1, subtarget+nums[idx])]
                
            if (idx+1,subtarget - nums[idx]) not in cache:
                minus = backtrack(idx+1, subtarget - nums[idx])
                cache[(idx+1, subtarget - nums[idx])] = minus
            else:
                minus = cache[(idx+1, subtarget - nums[idx])]
            
            return plus + minus
        
        return backtrack(0,0)
            