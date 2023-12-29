class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    
        def dfs(nums, target, subset, res):
            if target < 0:
                return 
            if target == 0:
                res.append(subset)
                return 
            for i in range(len(nums)):
                dfs(nums[i:], target-nums[i], subset+[nums[i]], res)
                
        res = []
        dfs(candidates, target, [], res)
        return res