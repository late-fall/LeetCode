class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for each item, we have a choice of including it or not
        # brute force is O(2^n) -> number of subsets
        
        # backtracking can be used. 
        res = []
        subset = [] # to add each to result
        def backtrack(n):
            if n == len(nums):
                res.append(subset.copy()) #subset will be modified otherwise.
                return
            
            # add the num
            subset.append(nums[n])
            backtrack(n+1)
            
            subset.pop()
            backtrack(n+1)
                    
        backtrack(0)
        
        return res
        
#         nums_idx = defaultdict(list)
#         subsets = []
        
#         # create a dictionary for location of each element in nums
#         for i,n in enumerate(nums):
#             subsets.append([n])
#             nums_idx[n] = i
        
#         # attach one element at a time starting from the last location.
#         while len(subsets[-1]) < len(nums):
#             for s in subsets:
#                 for n in nums[nums_idx[s[-1]]+1:]:
#                     subsets.append(s + [n])
        
#         subsets.append([])
        
#         return subsets