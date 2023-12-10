class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        
        for i, h in enumerate(height):
            while stack and h < height[stack[-1]]:
                ht = height[stack.pop()]
                wth = i - stack[-1] - 1
                ans = max(ans, ht * wth)
            stack.append(i)
        
        return ans