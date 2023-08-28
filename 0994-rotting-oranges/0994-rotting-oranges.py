class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        rots =[]
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    rots.append((x,y))
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def bfs(rots):
            q= deque()
            for r,c in rots:
                q.append((r,c))
            time = -1
            
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for dr,dc in directions:
                        if row + dr in range(rows) and col + dc in range(cols) and grid[row+dr][col+dc] == 1:
                            q.append((row+dr,col+dc))
                            grid[row+dr][col+dc] = 2
                time += 1
            
            return time
        
        t = 0
        t = max(t,bfs(rots))
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    return -1
        return t