class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def bfs(row,col):
            q = deque()
            q.append((row,col))
            cur = []
            vis.add((row,col))
            
            while q:
                x, y = q.popleft()
                for r,c in directions:
                    if (r+x) not in range(rows) or (c+y) not in range(cols):
                        return False
                    if (r+x,c+y) not in vis and board[x+r][y+c] == "O":
                        vis.add((r+x,c+y))
                        q.append((r+x,c+y))
            for r,c in vis:
                board[r][c] = "X"
            return True
            
        
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "O":
                    vis = set()
                    bfs(x,y)
                        