class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #minimum subset sum difference problem
        
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        
        stones.sort()
        n = len(stones)
        total = sum(stones)
        s = total//2
        
        dp = [[False for x in range(s+1)] for y in range(n)]
        
        for i in range(n):
            for j in range(s+1):
                if i == 0 and j > 0:
                    dp[0][j] = stones[i] == j
                if j == 0:
                    dp[i][0] = True
        
        for i in range(1,n):
            for j in range(1,s+1):
                if dp[i-1][j]:
                    dp[i][j] = True
                elif j >= stones[i]:
                    dp[i][j] = dp[i-1][j-stones[i]]
                    
        for i in range(s, -1, -1):
            if dp[n-1][i]:
                return abs(sum(stones) - i*2)