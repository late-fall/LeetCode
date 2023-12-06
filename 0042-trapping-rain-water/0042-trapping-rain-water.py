class Solution:
    def trap(self, height: List[int]) -> int:
        
        # height of water level at one point is min(max height of left, max height of right) - current height.
        # one way to solve is by creating an array of maxLeft, maxRight, and min(maxL, maxR)
        
        # trick is to use two pointers, left and right. Starting from each end.
        # set current leftMax and rightMax which is basically their respective values for now.
        # shift pointer which the max is smaller. 
        # for e.g., if ltMax <rtMax, we don't need to know what rtMax is since it doesn't affect equation.
        # water height will still be min(leftMax, rightMax) - height[i] where leftMax - height[i]
        
        lt, rt = 0, len(height) - 1
        ltMax = height[lt]
        rtMax = height[rt]
        
        water = 0
        
        while lt < rt:
            if ltMax <= rtMax:
                lt += 1
                ltMax = max(ltMax, height[lt])
                water += ltMax - height[lt]
            else:
                rt -= 1
                rtMax = max(rtMax, height[rt])
                water += rtMax - height[rt]
        
        return water
        