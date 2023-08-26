class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        rows = len(matrix) - 1
        while row < rows and target > matrix[row][0]:
            if row + 1 <= rows and target < matrix[row+1][0]:
                break
            row += 1
        
        l = 0
        r = len(matrix[0]) - 1
        
        print(matrix[row])
        
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
        
            