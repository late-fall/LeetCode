# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        levels = []
        level = 0
        
        def findLvl(root, level):
            if root:
                levels.append([root.val, level])
            if root.left:
                findLvl(root.left, level + 1)
            if root.right:
                findLvl(root.right, level + 1)
        
        findLvl(root, level)
        
        result = []
        
        for val in levels:
            if len(result) < val[1] + 1:
                result.append([val[0]])
            else:
                result[val[1]].append(val[0])
        return result