class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nmap = Counter(nums)
        for n in nmap:
            if nmap[n] > len(nums) // 2:
                return n