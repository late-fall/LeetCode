class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = {}
        back = {}
        total = len(nums)
        res = []
               
        front[0] = nums[0]
        for i in range(1,total):
            front[i] = front[i-1] * nums[i]
        
        back[total-1] = nums[total-1]
        for i in range(total-2, -1, -1):
            back[i] = back[i+1] * nums[i]
        
        for i in range(len(nums)):
            if i < 1:
                res.append(back[i+1])
            elif i >=len(nums) -1:
                res.append(front[i-1])
            else:
                res.append(back[i+1] * front[i-1])
        
        return res