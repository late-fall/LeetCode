class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        prev_color = image[sr][sc]
        # if prev_color == color: #need this to preven infinite recursion.
        #     return image
        def newcolor(r,c):
            if image[r][c] == prev_color and image[r][c] !=color:
                image[r][c] = color
                if r >= 1:
                    newcolor(r-1,c)
                if r + 1 < row:
                    newcolor(r+1,c)
                if c >= 1:
                    newcolor(r,c-1)
                if c+1 <col:
                    newcolor(r,c+1)
        newcolor(sr,sc)               
        
        return image