class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid_index = 0
        while len(nums) > 0 :
            mid = len(nums) // 2
            if target == nums[mid]:
                return mid + mid_index
            elif target > nums[mid]:
                mid_index += len(nums[:mid+1])
                nums = nums[mid+1:]
            else:
                target < nums[mid]
                nums = nums[:mid]
        return -1