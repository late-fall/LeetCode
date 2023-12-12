class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def findmidmax(nums):
            mid = len(nums) // 2
            cur_max_lt, cur_max_rt = -float('inf'), -float('inf')
            total_lt, total_rt = 0, 0
            for n in range(mid-1, -1, -1):
                total_lt += nums[n]
                cur_max_lt = max(cur_max_lt, total_lt)
            for n in range(mid, len(nums)):
                total_rt += nums[n]
                cur_max_rt = max(cur_max_rt, total_rt)
            
            return cur_max_lt + cur_max_rt
            
        
        def findmax(nums):
            if len(nums) == 1:
                return nums[0]
            mid = len(nums) // 2
            ltmax = findmax(nums[:mid])
            rtmax = findmax(nums[mid:])
            midmax = findmidmax(nums)
            
            return max(ltmax, rtmax, midmax)
            
        
        return findmax(nums)