class Solution:
    def jump(self, nums: List[int]) -> int:
        # idx, cnt = 0, 0 
        # while idx < len(nums) - 1:
        #     max_jump, max_idx = 0, 0 
        #     for i in range(1,nums[idx]+1):
        #         if i + idx >= len(nums):
        #             break
        #         if idx + nums[idx] >= len(nums) - 1 or i + nums[i+idx] >= max_jump:
        #             max_jump = i + nums[i+idx]
        #             max_idx = i
        #     idx += max_idx
        #     cnt += 1
        # return cnt
    
    #Other solution:
        res = 0 
        l = r = 0 # tell us the window
        # starts from 0,0, second lvl is l=1, r=2, etc..
        while r < len(nums) - 1:
            farthest = 0 # who can jump the farthest
            for i in range(l,r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res