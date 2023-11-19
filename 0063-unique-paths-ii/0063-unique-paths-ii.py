class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])

        dp = [[0 for col in range(c)] for row in range(r)]
        ob = []

        for x in range(r):
            for y in range(c):
                if obstacleGrid[x][y] == 1:
                    ob.append((x,y))
        
        for i in range(c):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        
        for i in range(r):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for x in range(1,r):
            for y in range(1,c):
                if (x,y) in ob:
                    dp[x][y] = 0
                else:
                    xway = dp[x-1][y]
                    yway = dp[x][y-1]
                    dp[x][y] = dp[x-1][y] + dp[x][y-1]

        return dp[r-1][c-1]
