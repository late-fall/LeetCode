class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for x in range(amount+1)] for y in range(n)]
        
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
        
        for c in range(1,n):
            for amt in range(1,amount+1):
                change1 = 0
                if coins[c] <= amt:
                    change1 = dp[c][amt-coins[c]]
                change2 = dp[c-1][amt]
                dp[c][amt] = change1 + change2               
        
        print(dp)
        
        return dp[n-1][amount]