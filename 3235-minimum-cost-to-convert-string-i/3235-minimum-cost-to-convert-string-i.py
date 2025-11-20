class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # DIJKSTRA
        n = len(source)
        INF = 10 ** 10
        graph = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            graph[u].append((v, w))
        
        print(graph)

        def dijkstra(start):
            dist = [INF] * 26
            dist[start] = 0
            pq = [(0, start)] # (dist, node)

            while pq:
                d, u = heapq.heappop(pq)
                for v, w in graph[u]:
                    if d + w < dist[v]:
                        dist[v] = d + w
                        heapq.heappush(pq, (dist[v], v))
            return dist
            
        # we want dist[u][v] cost from changing one letter to another for each letter
        # run dijkstra starting at each letter

        dist_all = [None] * 26

        for s in range(26):
            dist_all[s] = dijkstra(s)
        print(dist_all)
        
        total = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')

            cur_cost = dist_all[u][v]

            if cur_cost == INF:
                return -1
            total += cur_cost
        return total



