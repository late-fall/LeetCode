# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#[1,1]
#[5,4,6,null,null,3,7]
#[1,null,3]
#[5,1,6,null,null,4,7]
#[2,1,4,7,4,8,3,6,4,7]
#[10,5,15,null,null,6,20]
#[32,26,47,19,null,null,56,null,27]
#[0,-1]
#[5,4,5]
#[2147483647]
#[0,null,-1]
#[3,1,5,0,2,4,6]
#[-2147483648]

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, minimum, maximum):
            if not root:
                return True
            if root.val <= minimum or root.val >= maximum:
                return False
            return valid(root.left, minimum, root.val) and valid(root.right, root.val, maximum)
        return valid(root, (-2)**31 - 1, 2**31)