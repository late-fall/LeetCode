class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]: # when the new interval is smaller without overlapping
                return res + [newInterval] + intervals[i:] # return remaining interval with whatever was appended before.
            
            elif newInterval[0] > interval[1]: # when the new interval is greater without overlapping
                res.append(intervals[i])
                
            else: #overlapping, simply update the interval
                newInterval = [min(newInterval[0], interval[0]) , max(newInterval[1],interval[1])]
        
        res.append(newInterval)
        
        return res