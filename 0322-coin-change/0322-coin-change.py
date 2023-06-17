class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         can we be greedy? (pick biggest one first)
#         answer is NO. 
#         [1,3,4,5], sum up to Amount 7
#         start at 5 + 1 + 1 = 7
#         but the correct answer is 3 + 4. 
        
#         try DFS or backtracking?
#         [1,3,4,5]  amount = 7
#         goes like a tree
#         1,3,4,5 path, and keep going each
#         keep track of min Coin
        
#         top-down memoization, doing recursively
#         DP bottom up 
#         DP[0] = 0
#         DP[1] = 1
#         DP[2] = 1 + DP[1] = 2
#         .. and so on
#         repeat this process from DP[0] -> DP[7] = 1 + DP[6] = 3, but 1 + DP[4] = 2
        
    # O(amount * len(coins)) time
    # O(amount) memory
    
        dp = [amount + 1] * (amount + 1) # goes from 0..amount
        dp[0] = 0
        
        for a in range(1, amount +1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[amount] if dp[amount] != amount + 1 else - 1
        
#         num = 0
#         coins = sorted(coins)
        
#         def change(coins, amount, num):
#             if amount == 0:
#                 return num
#             if len(coins) == 0:
#                 return -1
#             if amount >= coins[-1]:
#                 return change(coins, amount - coins[-1], num + 1)
#             elif amount < coins[-1] and len(coins) <= 1:
#                 return change(coins[:-1], amount + coins[-1], num - 1)
#             else:
#                 return change(coins[:-1], amount, num)
#             return change
            
        
#         return change(coins, amount, num)