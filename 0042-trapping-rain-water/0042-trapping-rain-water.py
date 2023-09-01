class Solution:
    def trap(self, height: List[int]) -> int:
        waterset = set()
        
        l = 0 
        
        #set the starting point
        while l < len(height) and height[l] == 0:
            l += 1
            
        r = l + 1
        gr = 0
        water = 0
        while r < len(height):
            if height[r] >= height[l]:
                if r - l == 1:
                    l = r
                else:
                    waterset.add((l,r))
                    width = r - l - 1
                    water += width * min(height[r],height[l]) - gr
                    l = r
                    gr = 0
            else: 
                gr += height[r]
            
            r += 1
            
        b = len(height) - 1
        while r < len(height) and height[b] == 0:
            b -= 1
        f = b - 1
        gr = 0
        while f >= 0:
            if height[f] >= height[b]:
                if b - f == 1:
                    b = f
                else:
                    if (f,b) not in waterset:
                        width = b - f - 1
                        water += width * min(height[b],height[f]) - gr
                    b = f
                    gr = 0
            else:
                gr += height[f]
            
            f -= 1
        
        return water