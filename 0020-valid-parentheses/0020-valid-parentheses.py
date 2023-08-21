class Solution:
    def isValid(self, s: str) -> bool:
#         paren = []
#         for i in s:
#             if i == "(" or i == "{" or i == "[":
#                 paren.append(i)
#             if i == ")" or i == "}" or i == "]":
#                 if len(paren) == 0:
#                     return False
#                 p = paren.pop()
#                 if i == ")":
#                     if p != "(":
#                         return False
#                 if i == "}":
#                     if p != "{":
#                         return False
#                 if i == "]":
#                     if p != "[":
#                         return False
#         if len(paren) > 0:
#             return False
#         return True
        
#         NOTES
#         common interview question
#         try to use stack DS
#         hashmap
#         O(N), O(N)
        
#         NEETCODE
        parens = {")":"(","]":"[","}":"{"}
    
        stk = []
        
        for c in s:
            if c in parens:
                if not stk or parens[c] != stk.pop():
                    return False
            else:
                stk.append(c)
        
        return len(stk) == 0
                