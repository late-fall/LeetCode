# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and (left != p and left != q):
            return left
        if right and (right != p and right != q):
            return right
        if left and right:
            return root
        if left:
            return left
        return right
        
        
        # if not root:
        #     return
        # elif root.val == p.val or root.val == q.val:
        #     return root
        # l = self.lowestCommonAncestor(root.left, p, q) #l will be None or will return node when it's p or q.
        # r = self.lowestCommonAncestor(root.right, p, q)
        # if l and r: # if there's p or q in l AND r, it means root is the common ancestor
        #     return root
        # else:
        #     return l or r 