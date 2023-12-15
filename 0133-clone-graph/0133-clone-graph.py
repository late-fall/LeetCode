"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        q = deque()
        q.append(node)
        copies = {node.val: Node(node.val, [])}
        
        while q:
            cur = q.popleft()
            cur_copy = copies[cur.val]
            
            for nb in cur.neighbors:
                if nb.val not in copies:
                    copies[nb.val] = Node(nb.val, [])
                    q.append(nb)
                    
                cur_copy.neighbors.append(copies[nb.val])
        
        return copies[node.val]