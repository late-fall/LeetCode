class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        def dfs(i, intervals):
            if i >= len(intervals) -1 or not intervals[i+1]:
                return intervals[:i+1]
            if intervals[i][1] >= intervals[i+1][0]: 
                f1 = intervals[i][0]
                f2 = intervals[i][1]
                s1 = intervals[i+1][0]
                s2 = intervals[i+1][1]
                
                if s1 < f1:
                    if f2 >= s2:
                        return dfs(i, intervals[:i] + [[s1,f2]] + intervals[i+2:])
                    else:
                        return dfs(i, intervals[:i] + [[s1,f1]] + intervals[i+2:])
                else:
                    if f2 >= s2:
                        return dfs(i, intervals[:i] + [[f1,f2]] + intervals[i+2:])
                    else:
                        return dfs(i, intervals[:i] + [[f1,s2]] + intervals[i+2:])
            else:
                return dfs(i+1, intervals)
        
        return dfs(0, intervals)
    
        
#         # neet code solution
#         # tip: drawing picture for itnerval problem helps a lot. 
        
#         # O(nLogn) -> sorting time
#         intervals.sort(key = lambda i : i[0])
#         output = [intervals[0]]
        
#         for start, end in intervals[1:]:
#             lastEnd = output[-1][1]
            
#             if start <= lastEnd: #means overlapping
#                 output[-1][1] = max(lastEnd, end)
#             else:
#                 output.append([start,end]) # e.g.)
        
#         return output