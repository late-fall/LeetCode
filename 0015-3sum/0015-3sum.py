class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        dupset = set()
        
        for i in range(n-2):
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    subset = str(sorted([nums[i],nums[j],nums[k]]))
                    if subset not in dupset:
                        dupset.add(subset)
                        res.append((nums[i],nums[j],nums[k]))
                    j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    j += 1
        return res