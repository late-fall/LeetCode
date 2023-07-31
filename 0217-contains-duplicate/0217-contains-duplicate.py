class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = collections.defaultdict(int)
        for n in nums:
            if n in dic:
                return True
            else:
                dic[n] = n
        return False