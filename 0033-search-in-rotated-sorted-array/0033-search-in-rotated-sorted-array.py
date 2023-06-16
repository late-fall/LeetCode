class Solution:
    def search(self, nums: List[int], target: int) -> int:
        total = len(nums)
        if total == 1:
            return 0 if target == nums[0] else -1
        
        # index, value
        l = (0, nums[0])
        r = (total - 1, nums[total -1])
        
        while l[0] <= r[0]:
            mid = ((l[0] + r[0]) // 2, nums[(l[0] + r[0])//2])
            # print(mid)
            # print("left is ", end="")
            # print(l)
            # print("right is ", end="")
            # print(r)
            if mid[1] == target:
                return mid[0]
            if mid[0] == l[0] == r[0]:
                break
            if l[1] <= mid[1]:
                if target >= l[1] and target < mid[1]:
                    r = (mid[0] - 1, nums[mid[0] - 1])
                else:
                    l = (mid[0] + 1, nums[mid[0] + 1])
            elif l[1] > mid[1]:
                if target < mid[1] or target >= l[1]:
                    r = (mid[0] - 1, nums[mid[0] - 1])
                else:
                    l = (mid[0] + 1, nums[mid[0] + 1])
        
        return -1