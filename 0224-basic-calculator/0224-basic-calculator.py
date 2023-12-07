class Solution:
    def calculate(self, s: str) -> int:
        def addstk(op, num):
            if op == '+':
                stk.append(num)
            else:
                stk.append(-num)
        
        i = 0
        num = 0
        stk = []
        sign = '+'
        
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in '+-':
                addstk(sign, num)
                num, sign = 0, s[i]
            elif s[i] == '(':
                num, j = self.calculate(s[i +1:])
                i = i + j
            elif s[i] == ')':
                addstk(sign, num)
                return sum(stk), i + 1
            i += 1
        addstk(sign, num)
        
        return sum(stk)