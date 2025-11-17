class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        return True

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        n = len(vals)

        val_to_nodes = defaultdict(list)

        for node, val in enumerate(vals):
            val_to_nodes[val].append(node)
        
        print(graph)
        print(val_to_nodes)

        sorted_vals = sorted(val_to_nodes.keys())
        print(sorted_vals)
        dsu = DSU(n)
        ans = n
        for val in sorted_vals:

            for node in val_to_nodes[val]:
                for nei in graph[node]:
                    if vals[nei] <= val:
                        dsu.union(node, nei)
            
            # count how many nodes have value val in each connected component
            count = defaultdict(int)
            for node in val_to_nodes[val]:
                # In the component with representative root, we found one more node whose value is val
                root = dsu.find(node)
                count[root] += 1
            
            for k in count.values():
                ans += k * (k - 1) // 2
        return ans

