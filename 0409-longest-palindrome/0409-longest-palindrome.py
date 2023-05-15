class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c,0) + 1
        
        count = 0
        for v in hashmap.values():
            if v % 2 == 1:
                count += 1
        
        if count < 2:
            return len(s)
        else:              
            return len(s) - count + 1