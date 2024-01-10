class Solution:
    def maxProduct(self, s: str) -> int:
        # you can just brute force this problem as s.length max is 12
        # use bitmask
        
        n = len(s)
        pal = {}
        
        for mask in range(1, 2**n):
            subseq = ""
            for i in range(n):
                if mask & (2**i):
                    subseq += s[n - i - 1]
            if subseq == subseq[::-1]:
                pal[mask] = len(subseq)
        
        longest = 0
        for mask1 in pal:
            for mask2 in pal:
                if mask1 & mask2 == 0:
                    longest = max(longest, pal[mask1] * pal[mask2])
        
        return longest