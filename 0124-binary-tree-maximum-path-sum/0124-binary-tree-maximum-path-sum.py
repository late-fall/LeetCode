# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # function to find max value for a given node by going down a path
        # def maxpath(root, total):
        #     if not root:
        #         return
        #     total += root.val
        #     self.max_num = max(self.max_num,total)
        #     maxpath(root.left, total)
        #     maxpath(root.right, total)
        
        # self.res = -float('inf')

        # def dfs(root):
        #     if not root:
        #         return

        #     self.max_num = -float('inf')
        #     maxpath(root.left, 0)
        #     left = self.max_num if self.max_num > 0 else 0

        #     self.max_num = -float('inf')
        #     maxpath(root.right, 0)
        #     right = self.max_num if self.max_num > 0 else 0

        #     self.res = max(self.res, root.val + left + right)
        #     dfs(root.left)
        #     dfs(root.right)
        
        # dfs(root)

        # return self.res

        # NEETCODE way:
        res = [root.val]

        def findmax(root):
            if not root:
                return 0
            
            leftmax = max(findmax(root.left), 0)
            rightmax = max(findmax(root.right), 0)

            res[0] = max(res[0], root.val + leftmax + rightmax)

            return root.val + max(leftmax, rightmax)
        
        findmax(root)

        return res[0]