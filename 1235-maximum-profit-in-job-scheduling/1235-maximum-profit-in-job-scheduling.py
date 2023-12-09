class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        # use DP and sort the jobs by endTime
        # where dp[time] = profit indicates the max profit at given time. 
        # dp[0] = 0 as no profit can be made at time 0. 
        
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[1])
        dp = [[0,0]]
        for start, end, profit in jobs:
            prev_i = bisect.bisect(dp, [start+1]) - 1
            if dp[prev_i][1] + profit > dp[-1][1]:
                dp.append([end,dp[prev_i][1] + profit])
        return dp[-1][1]
    