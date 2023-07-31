class Solution:
    def rob(self, nums: List[int]) -> int:
                
        #think of house robber #1 problem, you can reuse this, on different subarray
        
        def rob1(nums):
            if not nums:
                return 0
            if len(nums) < 2:
                return nums[0]
            dp = collections.defaultdict(int)
            dp[0] = nums[0]
            dp[1] = max(dp[0], nums[1])
            for n in range(2,len(nums)):
                dp[n] = max(dp[n-1], dp[n-2]+nums[n])
            return dp[len(nums)-1]
    
        return max(nums[0],rob1(nums[1:]), rob1(nums[:-1]))