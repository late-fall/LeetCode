class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = defaultdict(int)
        for i in range(m+1):
            dp[(1,i)] = 1
        for j in range(n+1):
            dp[(j,1)] = 1
        
        if m > n:
            for r in range(2, m + 1):
                for c in range(1,n + 1):
                    dp[(r,c)] = dp[(r,c -1)] + dp[(r-1,c)]  
        else:
            for c in range(2, n + 1):
                for r in range(1,m + 1):
                    dp[(r,c)] = dp[(r,c -1)] + dp[(r-1,c)]  
        
        return dp[(m,n)]
        