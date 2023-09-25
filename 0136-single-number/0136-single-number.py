class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n not in nums[i+1:] + nums[:i]:
                return n
            