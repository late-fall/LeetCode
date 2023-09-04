class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        
        for x,y in points:
            d = x**2 + y **2
            heapq.heappush(pts,[d,[x,y]])
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(pts)[1])
        
        return res
            