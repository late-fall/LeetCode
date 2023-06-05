class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[99999 for x in range(n)] for y in range(m)]
        
#         check left and top
        for x in range(m):
            for y in range(n):
                if (mat[x][y] == 0):
                    res[x][y] = 0
                else:
                    if (x > 0):
                        res[x][y] = min(res[x][y], res[x-1][y] + 1)
                    if (y > 0):
                        res[x][y] = min(res[x][y], res[x][y-1] + 1)
                        
# check right and bottom
        for x in range(m-1, -1, -1):
            for y in range(n-1, -1, -1):
                if (mat[x][y] == 0):
                    res[x][y] = 0
                else:
                    if (x < m -1):
                        res[x][y] = min(res[x][y], res[x+1][y] + 1)
                    if (y < n - 1):
                        res[x][y] = min(res[x][y], res[x][y+1] + 1)

        return res