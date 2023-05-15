class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
            if hashmap[n] >= len(nums) / 2:
                return n