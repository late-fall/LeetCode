class Solution:
    def search(self, nums: List[int], target: int) -> int:
#         mid_index = 0
#         while len(nums) > 0 :
#             mid = len(nums) // 2
#             if target == nums[mid]:
#                 return mid + mid_index
#             elif target > nums[mid]:
#                 mid_index += len(nums[:mid+1])
#                 nums = nums[mid+1:]
#             else:
#                 target < nums[mid]
#                 nums = nums[:mid]
#         return -1
    
#     # very common to be asked. 
    
#     have two pointers
#     Left, Right. get mid point using (l+r)/2
    
        l, r = 0, len(nums) -1

        while l <= r: #when they are equal, they haven't evaluated yet. 
            m = (l + r) //2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1