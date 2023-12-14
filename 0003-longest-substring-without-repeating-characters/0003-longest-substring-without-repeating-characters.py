class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, longest = 0, 0, 0
        dic = collections.defaultdict(int)
        
        while r < len(s):
            dic[s[r]] += 1
            while dic[s[r]] > 1:
                dic[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest
                