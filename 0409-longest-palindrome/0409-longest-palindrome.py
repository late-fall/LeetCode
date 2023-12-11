class Solution:
    def longestPalindrome(self, s: str) -> int:
        sMap = Counter(s)
        total = 0
        odd = 0
        for ch in sMap.keys():
            if sMap[ch] % 2 == 1:
                odd += 1
            total += sMap[ch]
        
        odd = 0 if odd <= 1 else odd - 1
        return total - odd
        