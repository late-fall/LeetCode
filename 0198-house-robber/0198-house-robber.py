class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        dp = collections.defaultdict(int)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for n in range(2,len(nums)):
            dp[n] = max(dp[n-1], dp[n-2]+nums[n])
        return dp[len(nums)-1]