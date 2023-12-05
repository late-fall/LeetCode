class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        ltMax, rtMax = height[l], height[r]
        res = 0
        
        while l < r:
            if ltMax < rtMax:
                l += 1
                ltMax = max(ltMax, height[l])
                res += ltMax - height[l]
            else:
                r -= 1
                rtMax = max(rtMax, height[r])
                res += rtMax - height[r]
        return res
            
            