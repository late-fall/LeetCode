class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        
        def pacificBFS(row,col):
            q = deque()
            q.append((row,col))
            pvisited = set()
            pvisited.add((row,col))
            
            while q:
                r, c = q.popleft()
                if r - 1 < 0 or c - 1 < 0:
                    return True
                else:
                    if (r-1,c) not in pvisited and heights[r][c] >= heights[r-1][c]:
                        q.append((r-1,c))
                        pvisited.add((r-1,c))
                    if (r, c-1) not in pvisited and heights[r][c] >= heights[r][c-1]:
                        q.append((r,c-1))
                        pvisited.add((r,c-1))
                    if r + 1 < rows and (r+1, c) not in pvisited and heights[r][c] >= heights[r+1][c]:
                        q.append((r+1,c))
                        pvisited.add((r+1,c))
                    if c +1 <cols and (r, c+1) not in pvisited and heights[r][c] >= heights[r][c+1]:
                        q.append((r,c+1))
                        pvisited.add((r,c+1))
        
        def atlanticBFS(row,col):
            q = deque()
            q.append((row,col))
            avisited = set()
            avisited.add((row,col))
            
            while q:
                r, c = q.popleft()
                if r +1 >= rows or c + 1 >= cols:
                    return True
                else:
                    if (r+1,c) not in avisited and heights[r][c] >= heights[r+1][c]:
                        q.append((r+1,c))
                        avisited.add((r+1,c))
                    if (r, c+1) not in avisited and heights[r][c] >= heights[r][c+1]:
                        q.append((r,c+1))
                        avisited.add((r,c+1))
                    if r-1 >=0 and (r-1, c) not in avisited and heights[r][c] >= heights[r-1][c]:
                        q.append((r-1,c))
                        avisited.add((r-1,c))
                    if c-1 >= 0 and (r, c-1) not in avisited and heights[r][c] >= heights[r][c-1]:
                        q.append((r,c-1))
                        avisited.add((r,c-1))
        
        res = []
        for i in range(rows):
            for j in range(cols):
                if pacificBFS(i,j) and atlanticBFS(i,j):
                    res.append([i,j])
        return res
        
        