class Solution:
    def jump(self, nums: List[int]) -> int:
        idx = 0
        cnt = 0
        while idx < len(nums) - 1:
            max_jump = 0
            max_idx = 0
            for i in range(1,nums[idx]+1):
                if i + idx >= len(nums):
                    break
                if idx + nums[idx] >= len(nums) - 1:
                    max_idx = i
                if i + nums[i+idx] >= max_jump:
                    max_jump = i + nums[i+idx]
                    max_idx = i
            idx += max_idx
            cnt += 1
            print(idx, cnt)
        return cnt