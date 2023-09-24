class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        val = total // 2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == val:
                    return True
                nextDP.add(t+nums[i])
                nextDP.add(t)
            dp = nextDP
        return False

#         def dfs(i, target):
#             if target < 0 or i < 0:
#                 cache[target] = False
#                 return False
#             if target == 0:
#                 print('test')
#                 return True
#             if target in cache:
#                 print(target)
#                 return cache[target]
#             return dfs(i-1, target - nums[i]) or dfs(i-1, target)
        
#         return dfs(len(nums)-1,val)
    
#         def backtrack(i, subtotal):
#             if i >= len(nums) or subtotal > val:
#                 cache[subtotal] = False
#                 return False
#             subtotal += nums[i]
#             if subtotal == val:
#                 cache[subtotal] = True
#                 return True
#             if subtotal in cache:
#                 return cache[subtotal]
#             return backtrack(i+1, subtotal) or backtrack(i+1, subtotal - nums[i])
        
#         return backtrack(0,0)