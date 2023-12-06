import bisect

class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.idx = bisect.bisect_left(self.arr, num)
        self.arr = self.arr[:self.idx] + [num] + self.arr[self.idx:]

    def findMedian(self) -> float:
        n = len(self.arr)
        self.even = (n % 2 == 0)
        if not self.even:
            return float(self.arr[n//2])
        else:
            medians = self.arr[n//2-1:n//2+1]
            return (medians[0] + medians[1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()