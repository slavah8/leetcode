class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = defaultdict(list)
        ans = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, parent):
            counts = [0] * 26
            char = labels[node]
            label_idx = ord(char) - 97
            counts[label_idx] = 1
            
            
            for nei in graph[node]:
                if nei == parent:
                    continue
                child_counts = dfs(nei, node)
                for i in range(26):
                    counts[i] += child_counts[i]

            ans[node] = counts[label_idx]
            return counts
        
        dfs(0, -1)
        return ans