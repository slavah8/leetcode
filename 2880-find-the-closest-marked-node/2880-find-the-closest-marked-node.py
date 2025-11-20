class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
        
        INF = 10 ** 10
        dist = [INF] * n
        dist[s] = 0

        pq = [(0, s)] # (dist, node)

        while pq:
            print(pq)
            d, u = heapq.heappop(pq)
            if u in marked:
                return d
            for v, w in graph[u]:
                if w + dist[u] < dist[v]:
                    dist[v] = w + dist[u]
                    heapq.heappush(pq, (dist[v], v))
        return -1
                