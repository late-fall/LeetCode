"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # NeetCode solution:
        # use HashMap (like all graph problems)
#         hashmap of 1->1, 2->2, 3->3, and so on..
#         recursively start at node val of 1.
#         O(n) = number of edges + vertices
        
        oldToNew = {} #hashmap to map old to new
        
        def copyGraph(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(copyGraph(n))
            return copy
            
        return copyGraph(node) if node else None
        
        