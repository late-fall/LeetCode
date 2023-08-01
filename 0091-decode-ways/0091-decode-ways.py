class Solution:
    def numDecodings(self, s: str) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 1
        if s[0] == "0":
            return 0
        else:
            dp[1] = 1
        
        if len(s) == 1:
            return dp[1]
        
        for i in range(1,len(s)):
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            elif s[i-1] == "1" or (s[i-1] == "2" and int(s[i]) < 7 and int(s[i]) >0):
                dp[i+1] = dp[i-1] + dp[i]
            else:
                dp[i+1] = dp[i]
        return dp[len(s)]