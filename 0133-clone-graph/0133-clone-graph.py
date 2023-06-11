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
        
        def clone(node):
            if node in oldToNew: #means we already made a clone of it.
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            return copy
        
        return clone(node) if node else None
        
        # copy_node = Node()
        # def copyGraph(node):
        #     if len(node.neighbors) == 0:
        #         return []
        #     copy_node.val = node.val
        #     copy_node.neighbors = node.neighbors
        #     for n in node.neighbors:
        #         copyGraph(n)
        # copyGraph(node)
        
        # adjlist = []
        # node_adj = []
        # for n in node.neighbors:
        #     node_adj.append(n.val)
        # a = node_adj
        # print(a)
        return copy_node
        