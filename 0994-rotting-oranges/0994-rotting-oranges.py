class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh_count = 0
        rottens = []
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    fresh_count += 1
                elif grid[x][y] == 2:
                    rottens.append((x,y))
        
        directions = [[1,0], [-1,0], [0,-1],[0,1]]
        tmp = []
        minute = 0
        
        while rottens:
            for r,c in rottens:
                for dr, dc in directions:
                    if (r + dr) in range(rows) and (c + dc) in range(cols) and grid[r+dr][c + dc] == 1:
                        grid[r+dr][c+dc] = 2
                        fresh_count -= 1
                        tmp.append((r+dr,c+dc))
            if tmp:
                minute += 1
            rottens = tmp
            tmp = []
        
        return minute if fresh_count == 0 else -1
    
    
    # DFS won't work for this case. 
    # BFS is helpful. 
    # multi-source BFS
    # using queue data structure. 
    # keep track of how many fresh oranges there are 