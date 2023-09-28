class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        end = intervals[0][1]
        cnt = 0
        for i in range(1, len(intervals)):
            if end > intervals[i][0]: # overlapping
                cnt += 1
            else:
                end = intervals[i][1]
        return cnt