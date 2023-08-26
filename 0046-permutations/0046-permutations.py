class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(combo, cur):
            if len(cur) == 0:
                res.append(combo)
                return
            for i in range(len(cur)):
                a = cur[i]
                dfs(combo + [a], cur[:i] + cur[i+1:])
        
        dfs([],nums)
        
        return res
    
    