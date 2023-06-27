class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols
        res = []
        visited = set()
        
        r, c = 0, 0 
        
        while len(res) < total:
            while c < cols and (r,c) not in visited:
                res.append(matrix[r][c])
                visited.add((r,c))
                c += 1
            c -= 1
            r += 1
            while r < rows and (r,c) not in visited:
                res.append(matrix[r][c])
                visited.add((r,c))
                r += 1
            r -= 1
            c -= 1
            while c >= 0 and (r,c) not in visited:
                res.append(matrix[r][c])
                visited.add((r,c))
                c -= 1
            c += 1
            r -= 1
            while r >= 0 and (r,c) not in visited:
                res.append(matrix[r][c])
                visited.add((r,c))
                r -= 1
            r += 1
            c += 1
        return res