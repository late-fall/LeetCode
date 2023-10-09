class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        
        dp = [[0 for x in range(n1)] for y in range(n2)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        
        for i in range(1, n1):
            if dp[0][i-1] == 1:
                dp[0][i] = 1
            else:
                if text2[0] == text1[i]:
                    dp[0][i] = 1
                else:
                    dp[0][i] = 0
                    
        for i in range(1, n2):
            if dp[i-1][0] == 1:
                dp[i][0] = 1
            else:
                if text1[0] == text2[i]:
                    dp[i][0] = 1
                else:
                    dp[i][0] = 0
                
        for r in range(1,n2):
            for c in range(1,n1):
                if text1[c] == text2[r]:
                    dp[r][c] = dp[r-1][c-1] +1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        
        return dp[n2-1][n1-1]