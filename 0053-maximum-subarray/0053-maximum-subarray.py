class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#         1) can do brute force, calculate every subarray
#         - won't be very efficient, O(N^2)
#         "sliding window" - O(n)

        maxSub = nums[0]
        curSum = 0 #initial
        
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
        
#         first = nums[0]
#         second = nums[0]
        
#         for n in nums:
#             if n > 0:
#                 first += n
#             second += n
#             if first <second:
#                 first = second
                
        
#         return max(first,second);

        