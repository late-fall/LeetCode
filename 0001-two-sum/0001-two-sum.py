class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        for i in range(len(nums)):
            test = target - nums[i]
            for j in range(i+1,len(nums)):
                if test == nums[j]:
                    return [i,j]