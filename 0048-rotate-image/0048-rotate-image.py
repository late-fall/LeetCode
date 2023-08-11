class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r-l):
                top,bot = l, r
                
#                 temp = matrix[top][l+i]
#                 matrix[top][l+i] = matrix[bot-i][l]
#                 matrix[bot-i][l] = matrix[bot][r-i]
#                 matrix[bot][r-i] = matrix[top+i][r]
#                 matrix[top+i][r] = temp
                matrix[top][l+i], matrix[bot-i][l], matrix[bot][r-i], matrix[top+i][r] = matrix[bot-i][l], matrix[bot][r-i], matrix[top+i][r], matrix[top][l+i]
            l += 1
            r -= 1
        
#         visited = set()
        
#         def update(row, col):
#             val = matrix[row][col]
#             visited.add((row,col))
#             matrix[row][col] = matrix[cols - col - 1][row]
#             matrix[cols - col - 1][row] = val
            
        
#         for x in range(rows):
#             for y in range(cols):
#                 if (x,y) not in visited:
#                     update(x,y)