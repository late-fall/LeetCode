# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         while root:
#             que = deque()
#             que.append(root)
            
#             while que:
#                 node = que.popleft()
#                 minval = min(p.val,q.val)
#                 maxval = max(p.val,q.val)
#                 if node: 
#                     if p.val == node.val or q.val == node.val:
#                         return node
#                     if minval < node.val and maxval > node.val:
#                         return node
#                     que.append(node.left)
#                     que.append(node.right)
        
        def dfs(root):
            if not root:
                return
            if root.val == p.val or root.val == q.val:
                return root
            if min(p.val,q.val) < root.val and max(p.val,q.val) > root.val:
                return root
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)
                
