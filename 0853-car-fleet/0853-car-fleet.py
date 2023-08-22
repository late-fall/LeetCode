class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sec = []
        for i in range(len(position)):
            sec.append([position[i],speed[i], (target - position[i]) / speed[i]])
        
        sec.sort(key=lambda x: x[0])
        
        stk = []
        for s in sec:
            while stk and stk[-1] <= s[2]:
                stk.pop()
            stk.append(s[2])
        
        return len(stk)
            