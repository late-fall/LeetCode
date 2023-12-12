# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxht = 0
        
#         def getHt(root):
#             if not root:
#                 return -1
#             lt = getHt(root.left) + 1
#             rt = getHt(root.right) + 1
#             return max(lt, rt)
        
        def diameter(root):
            if not root:
                return -1
            lt_ht = diameter(root.left) + 1
            rt_ht = diameter(root.right) + 1
            d = lt_ht + rt_ht
            self.maxht = max(self.maxht, d)
            return max(lt_ht,rt_ht)
        
        diameter(root)
        return self.maxht