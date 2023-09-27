class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # first two conditions are when interval is NOT overlapping.
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else: #overlapping
                newInterval = [min(newInterval[0], intervals[i][0]),max(newInterval[1],intervals[i][1])]
        
        res.append(newInterval)
        
        return res