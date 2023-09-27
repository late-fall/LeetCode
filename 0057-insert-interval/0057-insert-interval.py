class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0 
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        int1, int2 = newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            int1 = min(intervals[i][0], int1)
            int2 = max(intervals[i][1], int2)
            i += 1
        res.append([int1,int2])
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res