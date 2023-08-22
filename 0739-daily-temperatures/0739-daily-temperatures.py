class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = [(temperatures[0],0)]
        output = [0] * len(temperatures)
        
        for i in range(1,len(temperatures)):
            while stk and temperatures[i] > stk[-1][0]:
                val, idx = stk.pop()
                output[idx] = i - idx
            stk.append((temperatures[i],i))
        
        return output