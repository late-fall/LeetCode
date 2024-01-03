class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def permutation(subset, num):
            if len(num) == 0:
                res.append(subset)
                return
            for i in range(len(num)):
                permutation(subset + [num[i]], num[:i] + num[i+1:])
        
        permutation([], nums)
        
        return res