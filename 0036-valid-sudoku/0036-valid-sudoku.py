class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for r in range(9):
            row = []
            rowset = set()
            for c in range(9):
                if board[r][c] != ".":
                    row.append(board[r][c])
                    rowset.add(board[r][c])
                if sorted(row) != sorted(list(rowset)):
                    return False
        
        # check col
        for c in range(9):
            col = []
            colset = set()
            for r in range(9):
                if board[r][c] != ".":
                    col.append(board[r][c])
                    colset.add(board[r][c])
                if sorted(col) != sorted(list(colset)):
                    return False
                
        for n in range(0,9,3):
            for x in range(9):
                if x % 3 == 0:
                    box = []
                    boxset = set()

                for y in range(3):
                    if board[x][y+n] != ".":
                        box.append(board[x][y+n])
                        boxset.add(board[x][y+n])

                if sorted(box) != sorted(list(boxset)):
                    return False
        
        return True