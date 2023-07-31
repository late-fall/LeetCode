class Solution:
    def countSubstrings(self, s: str) -> int:
        res = ""
        cnt = 0
        
        #for odd:
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res = s[l:r+1]
                cur_max = len(res)
                l -= 1
                r += 1
                cnt += 1
        
        #for even
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res = s[l:r+1]
                cur_max = len(res)
                l -= 1
                r += 1
                cnt += 1
        
        return cnt