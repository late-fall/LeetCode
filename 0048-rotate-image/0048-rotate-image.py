class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l, r = 0, len(matrix) - 1
        
        while l < r: # run the rotation
            for i in range(r - l): # need to do n - 1 rotations
                # i is handling the rotation by moving to the next value. 
                top, bottom = l, r
                
                # save top left value, serving as a temporary
                topLeft = matrix[top][l + i]
                
                # move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                matrix[bottom][r- i] = matrix[top+i][r]
                
                matrix[top+i][r] = topLeft
            
            # to do subproblem
            r -= 1
            l += 1
        
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