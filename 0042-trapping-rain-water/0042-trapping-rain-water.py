class Solution:
    def trap(self, height: List[int]) -> int:
        waterset = set()
        gr, water = 0, 0
        
        # run front to back. 
        l = 0 
        r = l + 1
        while r < len(height):
            if height[r] >= height[l]:
                if r - l >1:
                    waterset.add((l,r))
                    water += (r - l - 1) * min(height[r],height[l]) - gr
                    gr = 0
                l = r
            else: 
                gr += height[r]
            r += 1
        
        # run back to front. Make sure to omit the same water that was calculated
        b = len(height) - 1
        f = b - 1
        gr = 0
        while f >= 0:
            if height[f] >= height[b]:
                if b - f > 1:
                    if (f,b) not in waterset:
                        water += (b - f - 1) * min(height[b],height[f]) - gr
                    gr = 0
                b = f
            else:
                gr += height[f]
            f -= 1
        
        return water