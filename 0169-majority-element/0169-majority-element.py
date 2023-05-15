class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashmap = {}
        # for n in nums:
        #     hashmap[n] = hashmap.get(n, 0) + 1
        #     if hashmap[n] >= len(nums) / 2:
        #         return n
            
        # to make it more efficient, use Boyer_Moore algorithm:
#        more optimal as uses less memory
        
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res