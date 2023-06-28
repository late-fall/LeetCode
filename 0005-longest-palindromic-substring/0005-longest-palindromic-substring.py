class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Neetcode solution
        # checking if a string is a palindrome is linear time operation
        # brute force will be n^2, thus making (N^3)
        # another way is consider a center and expand outward (N^2)
        
        res = ""
        resLen = 0
        
        # odd length palindrome
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        # even length palindrome
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                
        return res
        

#         s_original = s
#         s_rev = s[::-1]
#         str_len = len(s)
#         longest = ""
#         for i in range(str_len):
#             cur_str = ""
#             for j in range(str_len):
#                 if s[j] == s_rev[j]:
#                     cur_str += s[j]
#                     if len(cur_str) > len(longest):
#                         longest = cur_str
#                 else:
#                     cur_str = ""
#             s = "." + s
#         s = s_original
#         for i in range(str_len):
#             cur_str = ""
#             for j in range(str_len):
#                 if s[j] == s_rev[j]:
#                     cur_str += s[j]
#                     if len(cur_str) > len(longest):
#                         longest = cur_str
#                 else:
#                     cur_str = ""
#             s_rev = '.' + s_rev
        
#         return longest