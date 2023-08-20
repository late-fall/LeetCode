class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = list(s)
        t1 = list(t)
        new_s = ""
        new_t = ""
        
        for c in s1:
            if c != "#":
                new_s += c
            else:
                new_s = new_s[:-1]
                
        for c in t1:
            if c != "#":
                new_t += c
            else:
                new_t = new_t[:-1]
        
        
        return new_s == new_t