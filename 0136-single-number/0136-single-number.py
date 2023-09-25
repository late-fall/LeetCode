class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for i, n in enumerate(nums):
        #     if n not in nums[i+1:] + nums[:i]:
        #         return n
        
        visit = set()
        for n in nums:
            if n in visit:
                visit.remove(n)
                continue
            visit.add(n)
        return list(visit)[0]
            