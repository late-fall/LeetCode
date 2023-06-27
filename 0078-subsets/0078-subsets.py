class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_idx = defaultdict(list)
        subsets = []
        
        for i,n in enumerate(nums):
            subsets.append([n])
            nums_idx[n] = i

        
        while len(subsets[-1]) < len(nums):
            for s in subsets:
                for n in nums[nums_idx[s[-1]]+1:]:
                    subsets.append(s + [n])
        
        subsets.append([])
        
        return subsets