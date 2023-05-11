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
    
#     # very common question.
    
#     have two pointers
#     Left, Right. get mid point using (l+r)/2
    
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2 # can be done by l + ((r-l) //2) to prevent overflow. 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1