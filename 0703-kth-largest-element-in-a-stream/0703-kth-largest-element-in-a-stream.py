class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.maxheap = []
        
        if len(nums) == 0:
            return 
        
        for i in range(min(k,len(self.nums))):
            heappush(self.maxheap, self.nums[i])
            
        for i in range(k,len(self.nums)):
            if self.nums[i] > self.maxheap[0]:
                heappop(self.maxheap)
                heappush(self.maxheap,nums[i])

    def add(self, val: int) -> int:
        if len(self.maxheap) == 0:
            heappush(self.maxheap,val)
        elif len(self.maxheap) < self.k:
            heappush(self.maxheap,val)
        elif val > self.maxheap[0]:
            heappop(self.maxheap)
            heappush(self.maxheap, val)
        return self.maxheap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)