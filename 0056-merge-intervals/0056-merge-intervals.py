class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        def dfs(i, intervals):
            if len(intervals) == 1 or i >= len(intervals) -1 or not intervals[i+1]:
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