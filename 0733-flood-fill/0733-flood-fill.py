class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        visited = set()
        initial = image[sr][sc]
        
        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in visited or image[r][c] == color or image[r][c] != initial:
                return
            image[r][c] = color
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        dfs(sr,sc)
        return image