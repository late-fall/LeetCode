# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
#         def checkSub(node1, node2):
#             if not node1:
#                 return False
#             if node1 == node2:
#                 return True
#             return checkSub(node1.left, node2) or checkSub(node1.right, node2)
            
#         if checkSub(p,q):
#             return p
#         if checkSub(q,p):
#             return q
  
        #leetcode solution for python
    
        if not root:
            return
        elif root.val == p.val or root.val == q.val:
            return root
        l = self.lowestCommonAncestor(root.left, p, q) #l will be None or will return node when it's p or q.
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r: # if there's p or q in l AND r, it means root is the common ancestor
            return root
        else:
            return l or r 
        
#         if root in (p,q):
#             return root
    
#         def findpath(root, node):
#             if not root.left or not root.right:
#                 return ['Not found']
#             if root.left == node:
#                 return [(root, "l")]
#             elif root.right == node:
#                 return [(root, "r")]
#             else:
#                 if root.left:
#                     p1 = [(root, "l")] + findpath(root.left, node)
#                     if p1[-1] != 'Not found':
#                         return p1
#                 if root.right:
#                     q1 = [(root, "r")] + findpath(root.right, node)
#                     if q1[-1] != 'Not found':
#                         return q1
        
#         p_path = findpath(root, p)
#         q_path = findpath(root, q)
        
        
#         for i in range(max(len(p_path),len(q_path))):
#             if i >= len(p_path):
#                 return q_path[i][0]
#             if i >= len(q_path):
#                 return p_path[i][0]
#             if p_path[i] != q_path[i]:
#                 return p_path[i][0]
        
                