class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        op = ["+", "-", "*", "/"]
        res = 0
        
        for token in tokens:
            if token not in op:
                stk.append(token)
            else:
                second = int(stk.pop())
                first = int(stk.pop())
                if token == "+":
                    stk.append(first + second)
                elif token == "-":
                    stk.append(first - second)
                elif token == "*":
                    stk.append(first * second)
                else:
                    stk.append(int(first / second))
        return int(stk[0])