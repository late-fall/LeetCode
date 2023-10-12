class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Greedy
        
        if sum(gas) < sum(cost):
            return -1
        
        total, start, idx = 0, 0, 0
        
        while start < len(gas):
            total += (gas[idx] - cost[idx])
            if total < 0:
                total = 0
                start = idx + 1
            idx += 1
            if idx == len(gas):
                return start
                
                
#         #TLE
#         start = -1
#         startings = []
#         for i in range(len(gas)):
#             if gas[i] >= cost[i]:
#                 startings.append(i)
        
#         for s in startings:
#             cnt = 0
#             g = 0
#             while cnt < len(gas):
#                 s = s % len(gas)
#                 g += gas[s]
#                 g -= cost[s]
#                 if g < 0:
#                     break
#                 cnt += 1
#                 s += 1
#             if cnt == len(gas):
#                 return s % len(gas)
            
#         return -1