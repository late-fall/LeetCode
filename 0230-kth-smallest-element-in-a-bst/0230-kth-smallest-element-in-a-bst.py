# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            
            vals = []
            
            def dfs(root,vals):
                if not root:
                    return
                if root.left:
                    dfs(root.left, vals)
                vals.append(root.val)
                if root.right:
                    dfs(root.right, vals)
            
            dfs(root, vals)
            return vals[k-1]