class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def paren(op, cp, p):
            if op == cp == n:
                res.append(p)
                return
            if op < n:
                paren(op + 1, cp, p + "(")
            if cp < op:
                paren(op, cp + 1, p + ")")
        
        paren(0,0, "")
        return res