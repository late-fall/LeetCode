class Solution:
    def trap(self, height: List[int]) -> int:
        
        # height of water level at one point is min(max height of left, max height of right) - current height.
        # one way to solve is by creating an array of maxLeft, maxRight, and min(maxL, maxR)
        
        # trick is to use two pointers, left and right. Starting from each end.
        # set current leftMax and rightMax which is basically their respective values for now.
        # shift pointer which the max is smaller. 
        # for e.g., if ltMax <rtMax, we don't need to know what rtMax is since it doesn't affect equation.
        # water height will still be min(leftMax, rightMax) - height[i] where leftMax - height[i]
        
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
            
            