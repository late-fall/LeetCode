class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, l, r):
            if not node:
                return True
            if not (node.val > l and node.val < r):
                return False
            
            return valid(node.right,node.val,r) and valid(node.left,l,node.val)
        
        return valid(root, -2**31-1, 2**31)