class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = 5001
        
        while l <= r:
            m = (l + r) //2
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
        
        
        # while l <= r:
        #     m = (l + r) // 2
        #     if nums[l] > nums[r]:
        #         if m < nums[r]:
        #             r = m - 1
        #         else:
        #             l = m + 1
        #     elif nums[l] < nums[r]:
        #         return nums[l]
        #     else:
        #         return nums[l+1]
        # return nums[0]