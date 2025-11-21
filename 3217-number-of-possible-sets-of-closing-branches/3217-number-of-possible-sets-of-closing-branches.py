class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        INF = 10 ** 10
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(start, mask):
            dist = [INF] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                cur_dist, u = heapq.heappop(pq)

                if cur_dist > dist[u]:
                    continue
                
                for v, w in graph[u]:
                    if not (mask & (1 << v)): # v is closed in this subset
                        continue
                    new_dist = cur_dist + w
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(pq, (new_dist, v))
            return dist

        ans = 0
        for mask in range(1 << n):
            active = [i for i in range(n) if mask & (1 << i)]
            
            if len(active) <= 1:
                ans += 1
                continue

            ok = True
            for s in active:
                dist = dijkstra(s, mask)
                for v in active:
                    if dist[v] > maxDistance:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                ans += 1
        return ans

                    
                    