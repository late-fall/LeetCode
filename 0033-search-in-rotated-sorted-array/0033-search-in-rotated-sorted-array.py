class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r) //2
            if target == nums[m]:
                return m
            
            # left portion?
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            
            # right portion?
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
                    
        
        # while l <= r:
        #     m = (l + r) // 2
        #     if target > nums[r]:
        #         if target > nums[m]:
        #             l = m + 1
        #         elif target < nums[m]:
        #             r = m - 1
        #         else:
        #             return m
        #     elif target < nums[r]:
        #         if target > nums[m]:
        #             r = m - 1
        #         elif target < nums[m]:
        #             l = m + 1
        #         else:
        #             return m
        #     else:
        #         return r
        # return -1