class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        def calc(op,num1, num2):
            if op == "+":
                return num1 + num2
            if op == "-":
                return num1 - num2
            if op == "*":
                return num1 * num2
            if op == "/":
                if num1 * num2 < 0:
                    return -(num1 // (-num2))
                return num1 // num2
        
        for t in tokens:
            if t in "+-*/":
                n2 = stk.pop()
                n1 = stk.pop()
                stk.append(calc(t,n1,n2))
            else:
                stk.append(int(t))
        
        return stk[0]