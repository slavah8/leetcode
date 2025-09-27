class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        if not edges:
            return 0

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        ans = 0
        def dfs(u, parent):

            nonlocal ans
            best1 = 0
            best2 = 0
            for v in graph[u]:
                if v == parent:
                    continue
                h = dfs(v, u) + 1
                if h > best1:
                    best2 = best1
                    best1 = h
                elif h > best2:
                    best2 = h
            ans = max(ans, best1 + best2)
            return best1


        dfs(edges[0][0], -1)
        return ans

        
        
