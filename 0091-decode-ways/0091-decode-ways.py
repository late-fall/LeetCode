class Solution:
    def numDecodings(self, s: str) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 1
        dp[1] = 1
                
        for i in range(len(s)):
            if s[i] == "0":
                if i == 0 or s[i-1] not in "12":
                    return 0
                else:
                    dp[i+1] = dp[i-1]
            elif s[i-1] == "1" or (s[i-1] == "2" and int(s[i]) < 7 and int(s[i]) >0):
                dp[i+1] = dp[i-1] + dp[i]
            else:
                dp[i+1] = dp[i]
        return dp[len(s)]