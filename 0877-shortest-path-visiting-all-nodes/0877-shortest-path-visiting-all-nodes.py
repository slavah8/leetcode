class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        n = len(graph)
        if n == 1:
            return 0
        FULL = (1 << n) - 1
        # 2D array where dist[u][mask] = shortest steps to be at node u 
        # having visited exactly the nodes in mask. -1 means unvisited

        dist = [[-1] * (1 << n) for _ in range(n)]
        q = deque()
        for u in range(n):
            m = 1 << u
            dist[u][m] = 0
            q.append((u, m))

        while q:
            node, mask = q.popleft()
            d = dist[node][mask]
            for nei in graph[node]:
                m = (1 << nei)
                new_mask = mask | m
                if dist[nei][new_mask] == -1:
                    dist[nei][new_mask] = 1 + d
                    if new_mask == FULL:
                        return dist[nei][new_mask]
                    q.append((nei, new_mask))
        return 0