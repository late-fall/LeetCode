# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxd = 0
        
        def depth(root):
            if not root:
                return 0
            lt = depth(root.left) + 1
            rt = depth(root.right) + 1
            d = max(lt, rt)
            self.maxd = max(self.maxd, d)
            return d
        
        depth(root)
        return self.maxd