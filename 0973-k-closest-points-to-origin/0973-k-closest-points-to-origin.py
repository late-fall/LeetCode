class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(x**2 + y**2, (x,y)) for x,y in points]
        heapify(dist)
        
        res = []
        for i in range(k):
            res.append(heappop(dist)[1])
        
        return res