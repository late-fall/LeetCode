class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        
        def backtrack(status, i):
            if i >= len(prices):
                return 0
            
            if (i, status) in dp:
                return dp[(i,status)]
            
            skip = backtrack(status, i+1)
                                    
            if status == 'short':
                dp[(i,status)] = max(backtrack('long', i+1) - prices[i], skip)
            elif status == 'long':
                dp[(i,status)] = max(backtrack('short', i + 2) + prices[i], skip)
            
            return dp[(i, status)]
        
        print(dp)
        return backtrack('short',0)