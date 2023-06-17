class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = {}
        dp[0] = [[]]
        dp[1] = []
        
        if target <2:
            return dp[target]
        
        for n in range(2,target+1):
            for c in candidates:
                if n not in dp:
                    dp[n] = []
                if n-c in dp and n-c >= 0 and n-c != 1:
                    for d in dp[n-c]:
                        dp[n].append(d + [c])
        
        for e in dp[target]:
            e.sort()
        
        result = []
        [result.append(x) for x in dp[target] if x not in result]
                
        return result