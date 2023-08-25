class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        candidates.sort()
        
        def backtrack(i, subset, t):
            if t <= 0 or i >= len(candidates):
                if t == 0:
                    res.append(subset[::])
                return
            subset.append(candidates[i])
            backtrack(i+1,subset, t - candidates[i])
            subset.pop()
            while i < len(candidates) - 1 and candidates[i+1] == candidates[i]:
                i += 1
            backtrack(i+1,subset, t)
        
        backtrack(0,[],target)
        return res