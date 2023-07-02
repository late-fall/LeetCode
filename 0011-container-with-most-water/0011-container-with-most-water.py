class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #Neetcode
        #O(N)
        # two pointer technique
        
        l, r = 0, len(height) - 1
        most = 0 
        
        while l < r:
            cur = min(height[l], height[r]) * (r - l)
            most = max(most,cur)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return most
        
        
        #correct, but time : N*N
        # most = 0
        # for i in range(len(height) - 1):
        #     for j in range(1,len(height)):
        #         cur = min(height[i], height[j]) * (j - i)
        #         most = max(most, cur)
        # return most
                