import bisect
from heapq import *

class MedianFinder:
    def __init__(self):
        self.minhp = []
        self.maxhp = []
        
    def addNum(self, num: int) -> None:
        heappush(self.minhp, -num)
        heappush(self.maxhp, -heappop(self.minhp))
        if len(self.maxhp) > len(self.minhp):
            heappush(self.minhp, -heappop(self.maxhp))
    
    def findMedian(self) -> float:
        if len(self.minhp) > len(self.maxhp):
            return float(-self.minhp[0])
        return (-self.minhp[0] + self.maxhp[0]) / 2
    
    
# one way to solve by using bisect
#     def __init__(self):
#         self.arr = []

#     def addNum(self, num: int) -> None:
#         self.idx = bisect.bisect_left(self.arr, num)
#         self.arr = self.arr[:self.idx] + [num] + self.arr[self.idx:]

#     def findMedian(self) -> float:
#         n = len(self.arr)
#         mid = n // 2
#         self.even = (n % 2 == 0)
#         if not self.even:
#             return float(self.arr[mid])
#         else:
#             medians = self.arr[mid-1:mid+1]
#             return (medians[0] + medians[1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()