class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        rows = len(image)
        cols = len(image[0])
        original = image[sr][sc]

        def fill(r, c, color):
            if r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in visited or image[r][c] != original:
                return
            image[r][c] = color
            visited.add((r,c))
            fill(r+1, c, color)
            fill(r-1, c, color)
            fill(r, c+1, color)
            fill(r, c-1, color)
        
        fill(sr,sc, color)

        return image
            