class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))
        
        pq = [(0, 0)]
        INF = 10 ** 10
        dist = [INF] * n
        dist[0] = 0

        while pq:
            cur_cost, u = heapq.heappop(pq)

            if u == n - 1:
                return cur_cost

            if cur_cost > dist[u]:
                continue
            
            for v, w in graph[u]:
                new_cost = cur_cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
        return -1

