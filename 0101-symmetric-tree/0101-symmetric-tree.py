# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(left, right):
            if left is None or right is None:
                return left == right
            if left.val != right.val:
                return False
            return symmetric(left.left, right.right) and symmetric(left.right, right.left)
        
        return symmetric(root.left, root.right)