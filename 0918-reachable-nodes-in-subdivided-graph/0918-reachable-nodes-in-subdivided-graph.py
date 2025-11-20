class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(list)
        for u, v, cnt in edges:
            w = cnt + 1
            graph[u].append((v, w))
            graph[v].append((u, w))
        INF = 10 ** 10
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)] # (dist, node)

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue

            for v, w in graph[u]:
                new_dist = d + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
        print(dist)
    
        reachable_original = sum(1 for d in dist if d <= maxMoves)

        reachable_subdivided = 0
        for u, v, cnt in edges:
            rem_u = max(0, maxMoves - dist[u]) if dist[u] <= maxMoves else 0
            rem_v = max(0, maxMoves - dist[v]) if dist[v] <= maxMoves else 0

            reachable_subdivided += min(cnt, rem_u + rem_v)
        return reachable_original + reachable_subdivided

            
