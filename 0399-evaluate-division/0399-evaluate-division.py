class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (x,y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1 /val
        
        print(graph)
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if end in graph[start]:
                return graph[start][end]
            
            for i in graph[start]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, end, visited)
                    if temp != -1:
                        return graph[start][i] * temp
            return -1.0
        
        res = []
        for q in queries:
            res.append(dfs(q[0], q[1], set()))
        return res
        
        
#         rates = {}
#         for i in range(len(equations)):
#             rates[equations[i][0]] = (equations[i][1], values[i])
#             rates[equations[i][1]] = (equations[i][0], 1 / values[i])
        
#         print(rates)
        
#         rate = 1
#         visited = set()
        
#         def dfs(start, end, rate):
#             if start in rates and rates[start][0] == end:
#                 return rate * rates[start][1]
#             if start not in visited:
#                 visited.add(start)
#                 if start not in rates:
#                     return -1
#                 else:
#                     rate *= rates[start][1]
#                     return dfs(rates[start][0], end, rate)
        
#         results = []
        
#         for q in queries:
#             results.append(dfs(q[0],q[1],rate))
        
#         return results
                                     