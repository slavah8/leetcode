class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # kahns algorithm but track leave nodes and keep peeling them off
        if n == 1:
            return [0]
        degree = [0] * n
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degree[u] += 1
            degree[v] += 1
        
        leaves = [i for i in range(n) if degree[i] == 1]
        print(leaves)
        print(graph)
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves


