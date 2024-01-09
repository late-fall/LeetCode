class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs, indeg = {}, {}
        
        for c in range(numCourses):
            preqs[c] = []
            indeg[c] = 0
        
        for e, s in prerequisites:
            preqs[s].append(e)
            indeg[e] += 1
        
        q = deque()
        
        for k in indeg.keys():
            if indeg[k] == 0:
                q.append(k)
                
        res = []
        
        while q:
            crs = q.popleft()
            res.append(crs)
            for next_crs in preqs[crs]:
                indeg[next_crs] -= 1
                if indeg[next_crs] == 0:
                    q.append(next_crs)
        
        return res if sum(indeg.values()) == 0 else []