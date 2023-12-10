class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        
        for p in s:
            if p in '([{':
                stk.append(p)
            else:
                if not stk:
                    return False
                last = stk.pop()
                if (p == ')' and last != '(') or (p==']' and last != '[') or (p == '}' and last != '{'):
                    return False
        
        return False if stk else True
                    
                    