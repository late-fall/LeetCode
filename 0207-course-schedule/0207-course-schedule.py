class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
# O(N+P) number of courses + prerequisites, need to visit every node and visit edges. 
        preHash = {i:[] for i in range(numCourses)} #create a hashmap for courses : prerequite(s)
        for course, prereqs in prerequisites:
            preHash[course].append(prereqs)
        
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            
            visited.add(crs)
            for pre in preHash[crs]:
                if not dfs(pre): 
                    return False
            
            visited.remove(crs)
            preHash[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
            
#         if len(prerequisites) >= numCourses:
#             return False
        
#         courses = []
#         pre_courses = [i[0] for i in prerequisites]
#         print(pre_courses)
        
#         def checkCycle(pre):
#             if pre[0] in courses:
#                 return False
#             courses.append(pre[0])
#             checkCycle([pre[1],pre[0]])        
        
#         for course in prerequisites:
#             checkCycle(course)
#             print('testing')
        
#         return True