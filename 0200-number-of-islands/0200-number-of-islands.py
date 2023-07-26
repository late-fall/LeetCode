class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        
        def bfs(grid, r, c):
            q = []
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                r, c = q.pop(0)
                if r + 1 < rows and grid[r+1][c] == "1" and (r+1,c) not in visited:
                    q.append((r+1, c))
                    visited.add((r+1,c))
                if r - 1 >= 0  and grid[r-1][c] == "1" and (r-1,c) not in visited:
                    q.append((r-1, c))
                    visited.add((r-1,c))
                if c + 1 < cols and grid[r][c+1] == "1" and (r,c+1) not in visited:
                    q.append((r, c+1))
                    visited.add((r,c+1))
                if c - 1 >= 0  and grid[r][c-1] == "1" and (r,c-1) not in visited:
                    q.append((r, c-1))
                    visited.add((r,c-1))
            
        cnt = 0 
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1" and (x,y) not in visited:
                    bfs(grid, x, y)
                    cnt += 1
        
        return cnt