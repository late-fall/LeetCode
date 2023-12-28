class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        count = 0
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    count += 1
                    dfs(x, y)
        
        return count