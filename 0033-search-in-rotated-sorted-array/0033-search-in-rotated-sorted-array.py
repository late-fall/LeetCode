class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # index, value
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if mid == l == r:
                break
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if target < nums[mid] or target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1