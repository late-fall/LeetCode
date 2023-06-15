# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
#         minVal = -2**31 -1
#         maxVal = 2**31

#         def isValid(root, minVal, maxVal):
#             if not root.left and not root.right:
#                 return True
#             elif not root.left:
#                 if root.right.val <= root.val or root.right.val >= maxVal:
#                     return False
#                 return isValid(root.right, root.val, maxVal)
#             elif not root.right:
#                 if root.left.val >= root.val or root.left.val <= minVal:
#                     return False
#                 return isValid(root.left, minVal, root.val)
#             else:
#                 if (root.left.val >= root.val or root.left.val <= minVal) or (root.right.val <= minVal or root.right.val >= maxVal):
#                     return False
#                 return isValid(root.left, root.left.val , maxVal) and isValid(root.right, minVal, root.right.val)
        
#         return isValid(root, minVal, maxVal)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, minimum, maximum):
            if not root:
                return True
            if root.val <= minimum or root.val >= maximum:
                return False
            return valid(root.left, minimum, root.val) and valid(root.right, root.val, maximum)
        return valid(root, (-2)**31 - 1, 2**31)