# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = []
        que.append(root)
        nodes = []
        while que:
            lvl = []
            for i in range(len(que)):
                node = que.pop(0)
                if node:
                    que.append(node.left)
                    que.append(node.right)
                    lvl.append(node.val)
            if len(lvl) > 0:
                nodes.append(lvl)
        return [x[-1] for x in nodes]