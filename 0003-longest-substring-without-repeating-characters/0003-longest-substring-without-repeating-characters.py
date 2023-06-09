class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest, cur = 0, 0
        # dic = {}
        # for c in s:
        #     if c not in dic:
        #         dic[c] = 1
        #         cur += 1
        #     else:
        #         dic = {}
        #         dic[c] = 1
        #         longest = max(longest,cur)
        #         cur = 1
        # longest = max(longest, cur)
        # return longest
        
        if len(s) <= 1:
            return len(s)
        
        longest = 1
        l, r = 0, 1
        temp = s[0]
        while r < len(s):
            if s[r] not in temp:
                temp += s[r]
                r += 1
            else:
                l += 1
                r = l + 1
                temp = s[l]
            longest = max(longest, r -l)
        return longest