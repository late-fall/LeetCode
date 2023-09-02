# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # a = root.val
        # b = subRoot.val
        
        
        def checksub(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False
            return checksub(root.left,subRoot.left) and checksub(root.right,subRoot.right)
        
        res = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                if node.val == subRoot.val:
                    if checksub(node,subRoot):
                        res.append(1)
                q.append(node.left)
                q.append(node.right)
        return 1 in res
        