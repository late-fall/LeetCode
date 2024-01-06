class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        names = {}
        graph = collections.defaultdict(set)
        
        for act in accounts:
            name = act[0]
            for email in act[1:]:
                graph[act[1]].add(email)
                graph[email].add(act[1])
                names[email] = name
        
        print('names: ', names)
        print('grpah: ', graph)
        
        connected, visited, i = collections.defaultdict(list), set(), 0
        
        def dfs(node, i):
            connected[i].append(node)
            visited.add(node)
            for nb in graph[node]:
                if nb not in visited:
                    dfs(nb, i)
        
        for email in graph:
            if email not in visited:
                dfs(email, i)
                i += 1
        
        print('connected components: ', connected)
                
        return [[names[val[0]]] + sorted(val) for _, val in connected.items()]