class Solution:
    def calculate(self, s: str) -> int:
        # goal is to add as an element to a stack and finally calculate its sum
        # if it has + or -, create a new element, * or / will be calculated right away to the last stack element.
        # use recursion when new () happens so treat it as a new function that spits out value at the end. 
        
        def stk_update(num, op):
            stk.append(num) if op == '+' else stk.append(-num)
        
        n = 0
        stk = []
        op = '+'
        i = 0
        
        while i < len(s):
            if s[i].isdigit():
                n = n * 10 + int(s[i])
            elif s[i] in '+-':
                stk_update(n, op)
                n = 0
                op = s[i]
            elif s[i] == '(':
                n, j = self.calculate(s[i+1:])
                i += j
            elif s[i] == ')':
                stk_update(n, op)
                return sum(stk), i + 1
            i += 1
        stk_update(n, op)
        return sum(stk)
        