class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        # NEETCODE sol.
        # 1. capture unsurrounded (O -> T)
        # 2. capture surround regions (convert O -> X)
        # 3. uncapture unsurrounded (T -> O) as per requirement
        
        def dfs(r,c):
            if r < 0 or c <0 or r == rows or c == cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and r in [0,rows-1] or c in [0,cols-1]: # border cell
                    dfs(r,c)
                
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
                
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
        
        
#         directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
#         def bfs(row,col):
#             q = deque()
#             q.append((row,col))
#             cur = []
#             vis.add((row,col))
            
#             while q:
#                 x, y = q.popleft()
#                 for r,c in directions:
#                     if (r+x) not in range(rows) or (c+y) not in range(cols):
#                         return False
#                     if (r+x,c+y) not in vis and board[x+r][y+c] == "O":
#                         vis.add((r+x,c+y))
#                         q.append((r+x,c+y))
#             for r,c in vis:
#                 board[r][c] = "X"
#             return True
            
        
#         for x in range(rows):
#             for y in range(cols):
#                 if board[x][y] == "O":
#                     vis = set()
#                     bfs(x,y)
                        