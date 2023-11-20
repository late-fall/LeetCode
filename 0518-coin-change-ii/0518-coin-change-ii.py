class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(amount + 1):
            dp[0][i] = 1 if (coins[0] <= i and i % coins[0] == 0 or i==0) else 0
        
        for i in range(1,n):
            for j in range(1,amount + 1):
                if j >= coins[i]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
                else:
                    dp[i][j] = dp[i-1][j]
            
        return dp[n-1][amount]