class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        
        def back(i):
            if i == len(s):
                res.append(subset[::])
                return
            for j in range(i,len(s)):
                if ispal(s[i:j+1]):
                    subset.append(s[i:j+1])
                    back(j+1)
                    subset.pop()
        
        
        def ispal(s):
            l, r = 0, len(s) - 1
            while l < r:
                if not s[l] == s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        back(0)
        return res