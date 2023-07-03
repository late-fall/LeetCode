class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:        
        rows = len(board)
        cols = len(board[0])
        visited = set()
        
        def checkWord(r,c,word):
            if board[r][c] == word:
                return True
            if len(word) == 1 and board[r][c] != word:
                return False
            directions = [(0,1), (1,0), (-1, 0), (0, -1)]
            for dr, dc in directions:
                visited.add((r,c))
                if (dr + r) in range(rows) and (dc + c) in range(cols) and (dr+r,dc+c) not in visited and word[1] == board[dr+r][dc+c]:
                    result = checkWord(dr+r, dc+c, word[1:])
                    if result:
                        return True
                else:
                    visited.remove((r,c))
    
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited.clear()
                    if checkWord(i,j,word):
                        return True
        return False
    
    
        #O(n * m * 4^len(word)) : since looking at 4 directions for length of word
        