class Solution:
    def jump(self, nums: List[int]) -> int:
        idx, cnt = 0, 0 
        while idx < len(nums) - 1:
            max_jump, max_idx = 0, 0 
            for i in range(1,nums[idx]+1):
                if i + idx >= len(nums):
                    break
                if idx + nums[idx] >= len(nums) - 1 or i + nums[i+idx] >= max_jump:
                    max_jump = i + nums[i+idx]
                    max_idx = i
            idx += max_idx
            cnt += 1
        return cnt