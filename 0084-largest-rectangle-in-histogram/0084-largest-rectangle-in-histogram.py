import heapq

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stk = [] # holds pair of element (idx, ht)
        
        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                idx, ht = stk.pop()
                maxArea = max(maxArea, ht * (i - idx))
                start = idx
            stk.append((start,h))
        
        for i, h in stk:
            maxArea = max(maxArea, h * (len(heights)-i))
        
        return maxArea
        
        
        
#         min_ht = math(inf)
#         max_area = 0
#         stk = []
#         last = -1
        
#         for i in range(len(heights)):
#             min_ht = min(min_ht, heights[i])
#             area1 = min_ht * (i - last)
#             area2 = 
#             if stk and stk[-1][0] <= area:
#                 stk.pop()
#             stk.append((area,heights[i]))
            
#         return area
            