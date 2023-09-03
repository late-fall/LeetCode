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
            count = dfs(root.left, maxval) + dfs(root.right, maxval)
            return count if root.val < maxval else count + 1
        
        return dfs(root, root.val)