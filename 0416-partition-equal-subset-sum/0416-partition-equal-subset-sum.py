class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #NEETCODE solution
#         total = sum(nums)
#         if total % 2 == 1:
#             return False
#         val = total // 2
#         dp = set()
#         dp.add(0)
        
#         for n in nums:
#             nextDP = set()
#             for t in dp:
#                 if (t + n) == val:
#                     return True
#                 nextDP.add(t+n)
#                 nextDP.add(t)
#             dp = nextDP
#         return False

        t = sum(nums)
        if t % 2 == 1:
            return False
        t = t // 2
        n = len(nums)
        
        dp = [[False for x in range(t+1)] for y in range(n)]
        
        for i in range(n):
            dp[i][0] = True
        
        for i in range(1,t+1):
            dp[0][i] = (nums[0] == i)
            # for 1 item only, see if it's same as the target.
        
        for i in range(1, n):
            for s in range(1, t+1):
                if dp[i-1][s]:
                    dp[i][s] = True
                elif s >= nums[i]:
                    dp[i][s] = dp[i-1][s - nums[i]]
        
        return dp[n-1][t]
        
            
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