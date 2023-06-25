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
        stack= []
        closeToOpen = {")": "(", "]":"[","}":"{"}
        open = {"(", "[", "{"}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            elif c in open:
                stack.append(c)
        return True if not stack else False #to make sure it's empty 