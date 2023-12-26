class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #topological sorting
        graph = {n : [] for n in range(numCourses)}
        indeg = [0] * numCourses
        
        for c, p in prerequisites:
            graph[p].append(c)
            indeg[c] += 1
            
        q = deque()
        # if indeg is 0, we can start from here
        for n in range(numCourses):
            if indeg[n] == 0:
                q.append(n)
                
        num = len(q)
        while q:
            start = q.popleft()
            for dest in graph[start]:
                indeg[dest] -= 1
                if indeg[dest] == 0:
                    num += 1
                    q.append(dest)
        
        return num == numCourses
        