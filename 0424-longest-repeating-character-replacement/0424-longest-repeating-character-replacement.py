class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def restVal(chr_dict):
            return sum(chr_dict.values()) - max(chr_dict.values())
        
        start = 0
        longest = 0
        chars = collections.defaultdict(int)
        
        for end in range(len(s)):
            chars[s[end]] += 1
            
            while len(chars) > k + 1 or restVal(chars) > k:
                chars[s[start]] -= 1
                if chars[s[start]] == 0:
                    del chars[s[start]]
                start += 1
            
            longest = max(longest, end - start + 1)
        
        return longest