# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxval):
            if not root:
                return 0
            maxval = max(root.val, maxval)
            if root.val >= maxval:
                return dfs(root.left, maxval) + dfs(root.right, maxval) + 1
            else:
                return dfs(root.left, maxval) + dfs(root.right, maxval)
        
        return dfs(root, root.val)