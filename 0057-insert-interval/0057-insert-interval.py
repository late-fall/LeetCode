class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         drawing picture helps
#       time O(n), memory O(n)
        
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
        
        # first, second = None, None
        # found_first = False
        # new_first = newInterval[0]
        # new_second = newInterval[1]
        # for i in range(len(intervals)):
        #     cur_first = intervals[i][0]
        #     cur_second = intervals[i][1]
        #     if new_first > cur_first:
        #         continue
        #     if not found_first:
        #         if new_first < cur_first:
        #             if new_second < cur_first:
        #                 print('test1')
        #                 return [newInterval] + intervals
        #             elif new_second == cur_first:
        #                 print('test2')
        #                 return [new_first, cur_second] + intervals[1:]
        #             found_first = True
        #             first = i
        #         if new_first == cur_first:
        #             if new_second <= cur_second:
        #                 print('test3')
        #                 return intervals
        #             found_first = True
        #             first = i
        #     else:
        #         if new_second <= cur_second:
        #             second = i
        # if first and second:
        #     return intervals[first:] + [intervals[first][0],intervals[second][1]] + intervals[:second]
        # else:
        #     return intervals + newInterval