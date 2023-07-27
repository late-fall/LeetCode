class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # use BFS approach
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(r, c):
            q = []
            q.append((r,c))
            visited.add((r,c))
            area = 1

            while q:
                row, col = q.pop(0)
                if row + 1 < rows and grid[row+1][col] == 1 and (row+1,col) not in visited:
                    q.append((row+1,col))
                    visited.add((row+1,col))
                    area += 1
                if row - 1 >= 0 and grid[row-1][col] == 1 and (row-1,col) not in visited:
                    q.append((row-1,col))
                    visited.add((row-1,col))
                    area += 1
                if col + 1 < cols and grid[row][col+1] == 1 and (row,col +1) not in visited:
                    q.append((row,col+1))
                    visited.add((row,col+1))
                    area += 1
                if col -1 >= 0 and grid[row][col-1] == 1 and (row,col-1) not in visited:
                    q.append((row,col-1))
                    visited.add((row,col-1))
                    area += 1
                    
            return area


        max_area = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and (x,y) not in visited:
                    max_area = max(max_area,bfs(x, y))
        
        return max_area