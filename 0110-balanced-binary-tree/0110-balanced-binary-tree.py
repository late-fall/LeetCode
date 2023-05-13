# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #try to return 2 values on separate function
        # [boolean, ht]
        # recursive calls which returns boolean and ht value
        # if every false anywhere, it will return false.
        def checkBal(root):
            if not root: return [True,0]
            left, right = checkBal(root.left), checkBal(root.right)
            is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [is_balanced, 1 + max(left[1],right[1])]
        return checkBal(root)[0]