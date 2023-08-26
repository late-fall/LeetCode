class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = [] # current partition
        
        def dfs(i):
            if i >=len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if ispal(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        def ispal(s):
            l, r = 0, len(s) - 1
            while l < r:
                if not s[l] == s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        dfs(0)
        return res
        
#         def backtrack(i, subset, s):
#             if i == len(s):
#                 res.append(subset)
#                 return
            
#             backtrack(i,subset + s[i],s[1:])
#             backtrack(i,)