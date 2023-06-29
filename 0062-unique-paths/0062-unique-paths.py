class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = defaultdict(int)
        for i in range(max(m,n)+1):
            dp[(1,i)] = 1
            dp[(i,1)] = 1
        
        for r in range(2, m + 1):
            for c in range(1,n + 1):
                dp[(r,c)] = dp[(r,c -1)] + dp[(r-1,c)]  
        return dp[(m,n)]
        
        #NEETcode
        # DFS
        # have cache[r][c], if reach this point, no need for DFS again. 
        # result = Right + Down
        # base position = 1, number of ways to reach ending poistion is 1.
#         row = [1] * n
        
#         for i in range(m - 1):
#             newRow = [1] * n
#             for j in range(n - 2, -1, -1):
#                 newRow[j] = newRow[j + 1] + row[j]
#             row = newRow
#         return row[0]