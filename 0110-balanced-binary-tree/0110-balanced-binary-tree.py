# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHt(root):
            if not root:
                return -1
            ht_lt = getHt(root.left) + 1
            ht_rt = getHt(root.right) + 1
            return max(ht_lt, ht_rt)
        
        def checkBal(root):
            if not root:
                return True
            if abs(getHt(root.left) - getHt(root.right)) > 1:
                return False
            return checkBal(root.left) and checkBal(root.right)
        
        return checkBal(root)