class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        d1 = Counter(s1)
        d2 = Counter(s2[:len(s1)])
        
        l = 0
        r = len(s1) - 1
        
        while r < len(s2):
            if d1 == d2:
                return True
            d2[s2[l]] -= 1
            l += 1
            r += 1
            if r < len(s2):
                d2[s2[r]] += 1
        
        return False
            
                