class Solution:
    def longestPalindrome(self, s: str) -> str:
        # consider odd and even palindrome, which will be calculated differently. 
        
        res = ""
        cur_max = 0
        
        #for odd:
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > cur_max:
                    res = s[l:r+1]
                    cur_max = len(res)
                l -= 1
                r += 1
        
        #for even
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > cur_max:
                    res = s[l:r+1]
                    cur_max = len(res)
                l -= 1
                r += 1
        
        return res