class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        
        def backtrack(i):
            if i == len(s):
                res.append(part[::])
                return
            for j in range(i,len(s)):
                if ispal(s[i:j+1]):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
        
        def ispal(s):
            l, r = 0, len(s) - 1
            while l < r:
                if not s[l] == s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        backtrack(0)
        return res