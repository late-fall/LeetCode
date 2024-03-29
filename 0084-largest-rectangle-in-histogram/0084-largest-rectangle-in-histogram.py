class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = []
        ans = 0
        
        for i in range(len(height)):
            while stack and height[i] < height[stack[-1]]:
                ht = height[stack.pop()]
                wth = i if not stack else i - stack[-1] - 1
                ans = max(ans, ht * wth)
            stack.append(i)
        
        return ans