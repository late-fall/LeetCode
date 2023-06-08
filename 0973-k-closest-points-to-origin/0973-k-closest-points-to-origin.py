class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         using minHeap
#         Heapify - linear time algorithm
# add them to minHeap and pop k times.
        minHeap = []
        for x,y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist,x,y])
        
        heapq.heapify(minHeap) #heapify the list
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res
        
# #         works but goes overtime
#         res = [(points[0], points[0][0]**2 + points[0][1]**2)]
#         final = [points[0]]
#         for pt in points[1:]:
#             dist = pt[0]**2 + pt[1]**2
#             if len(res) > k:
#                 if res[k][1] < dist:
#                     continue
#             i = 0
#             while i <len(res) and res[i][1] < dist:
#                 i+=1
#                 if i > k:
#                     break
#             if i <= k:
#                 res.insert(i, (pt,dist))
#                 final.insert(i,pt)
#         return final[:k]