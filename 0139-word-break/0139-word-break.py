class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(1,len(s)+1):
            for w in wordDict:
                if len(w) <= i and s[i-len(w):i] == w and dp[i-len(w)] == True:
                    dp[i] = True
                    break
            else:
                dp[i] = False
        return dp[-1]