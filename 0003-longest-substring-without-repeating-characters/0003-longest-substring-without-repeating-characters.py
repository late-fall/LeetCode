class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        chr_dict = collections.defaultdict(int)
        
        for end in range(len(s)):
            chr_dict[s[end]] += 1
            
            while chr_dict[s[end]] > 1:
                chr_dict[s[start]] -= 1
                start += 1
            
            longest = max(longest, end - start +1)
        
        return longest