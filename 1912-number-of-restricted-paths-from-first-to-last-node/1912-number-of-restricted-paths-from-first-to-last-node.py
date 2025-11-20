class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        INF = 10 ** 10
        dist = [INF] * (n + 1)
        dist[n] = 0

        pq = [(0, n)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            
            for v, w in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(pq, (d + w, v))
        print(dist)

        memo = [-1] * (n + 1)

        def dfs(u):
            if u == n:
                return 1
            if memo[u] != -1:
                return memo[u]

            total = 0
            for v, _ in graph[u]:
                if dist[v] < dist[u]:
                    total += dfs(v)
                    if total >= MOD:
                        total -= MOD
            
            memo[u] = total
            return memo[u]
        
        return dfs(1)
