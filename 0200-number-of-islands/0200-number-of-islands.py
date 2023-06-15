class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#         BFS
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0,1], [0,-1]]
                for dr, dc in directions:
                    if ((row + dr) in range(rows) and (col + dc) in range(cols) and grid[row + dr][col + dc] == "1" and (row + dr, col + dc) not in visited):
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
    
        
#         m = len(grid[0])
#         n = len(grid)
        
#         grid = [list( map(int,i) ) for i in grid]
#         islands = 0
        
#         for x in range(n):
#             for y in range(m):
#                 if grid[x][y] >= 1:
#                     if not ((x > 0 and grid[x-1][y] >= 1) or (y > 0 and grid[x][y-1] >= 1)):
#                         if not ((x < n -1 and grid[x+1][y] > 1) or (y < m - 1 and grid[x][y+1] > 1)):
#                             islands += 1
#                     if (x < n -1 and grid[x+1][y] >= 1):
#                         grid[x+1][y] += 1
#                     if (y < m -1 and grid[x][y+1] >= 1):
#                         grid[x][y+1] += 1
#         return islands
    
    
    
     # elif x < n - 1 and grid[x+1][y] == "1":
     #     continue
    
     # elif y < m - 1 and grid[x][y+1] == "1":
     #     continue