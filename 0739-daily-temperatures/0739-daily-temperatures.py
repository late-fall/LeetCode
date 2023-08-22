class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        output = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stk and temperatures[i] > stk[-1][0]:
                val, idx = stk.pop()
                output[idx] = i - idx
            stk.append((temperatures[i],i))
        
        return output