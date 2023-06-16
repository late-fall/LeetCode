class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid[0])
        cols = len(grid)
        
        fresh_count = 0
        rottens = []
        
        for x in range(cols):
            for y in range(rows):
                if grid[x][y] == 1:
                    fresh_count += 1
                elif grid[x][y] == 2:
                    rottens.append((x,y))
        
        directions = [[1,0], [-1,0], [0,-1],[0,1]]
        tmp = []
        minute = 0
        rotten_count = len(rottens)
        total_orange = fresh_count + rotten_count
        
        while rottens:
            for r,c in rottens:
                for dr, dc in directions:
                    if (r + dr) in range(cols) and (c + dc) in range(rows) and grid[r+dr][c + dc] == 1:
                        grid[r+dr][c+dc] = 2
                        rotten_count += 1
                        tmp.append((r+dr,c+dc))
            if tmp:
                minute += 1
            rottens = tmp
            tmp = []
        
        return minute if total_orange == rotten_count else -1