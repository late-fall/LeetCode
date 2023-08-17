class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        
        if len(s1) > len(s2):
            return False
        
        for c in s1:
            d1[c] += 1
        for i in range(len(s1)):
            d2[s2[i]] += 1
        
        l = 0
        r = len(s1) - 1
        
        while r < len(s2):
            if d1 == d2:
                return True
            d2[s2[l]] -= 1
            if d2[s2[l]] == 0:
                del d2[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                d2[s2[r]] += 1
        
        return False
            
                