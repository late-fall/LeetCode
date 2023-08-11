class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        
        for n in nums:
            cur = 0
            if (n-1) not in numSet: # this is the starting point of a sequence
                while (n + cur) in numSet: #checking towards the right side
                    cur += 1
            longest = max(longest, cur)
        
        return longest