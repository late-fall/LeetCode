# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        
#         def checksub(root,subRoot):
#             if not root and not subRoot:
#                 return True
#             if not root or not subRoot or root.val != subRoot.val:
#                 return False
#             return checksub(root.left,subRoot.left) and checksub(root.right,subRoot.right)
        
#         q = deque()
#         q.append(root)
#         while q:
#             node = q.popleft()
#             if node:
#                 if node.val == subRoot.val:
#                     if checksub(node,subRoot):
#                         return True
#                 q.append(node.left)
#                 q.append(node.right)
#         return False
        
        if not t:
            return True
        if not s:
            return False
        if self.sameTree(s,t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False