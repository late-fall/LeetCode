class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = collections.defaultdict(set)
        for src, dst in edges:
            adj[src].add(dst)
            adj[dst].add(src)
        
        leaves = [x for x in range(n) if len(adj[x]) == 1]
        removal = len(leaves)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                # removing leaf nodes
                nb = adj[leaf].pop()
                adj[nb].remove(leaf)
                # add to new_leaves to be removed if its degree is 1.
                if len(adj[nb]) == 1:
                    new_leaves.append(nb)
            leaves = new_leaves
        return leaves