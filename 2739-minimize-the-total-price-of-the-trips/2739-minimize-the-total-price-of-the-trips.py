class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        

        def dfs(u, end, parent, path):
            path.append(u)
            if u == end:
                return True

            for v in graph[u]:
                if v == parent:
                    continue
                if dfs(v, end, u, path):
                    return True
            path.pop()
            return False

        freq = [0] * n
        
        for s, e in trips:
            path = []
            dfs(s, e, -1, path)
            for node in path:
                freq[node] += 1
        print(freq)
    
        # dp0[u] = minimum total cost of the entire subtree rooted at u assuming we did not halve at u
        dp0 = [0] * n
        dp1 = [0] * n
        def dfs_dp(u, parent):
            full_cost = freq[u] * price[u]
            half_cost = freq[u] * (price[u] // 2)

            dp0[u] = full_cost
            dp1[u] = half_cost
            for v in graph[u]:
                if v == parent:
                    continue
                dfs_dp(v, u)
                
                dp0[u] += min(dp0[v], dp1[v])
                dp1[u] += dp0[v]
        
        dfs_dp(0, -1)
        print(dp0)
        print(dp1)
        return min(dp0[0], dp1[0])
        