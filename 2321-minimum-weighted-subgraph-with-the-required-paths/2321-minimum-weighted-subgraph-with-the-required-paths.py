class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        INF = 10 ** 10
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            reverse_graph[v].append((u, w))
            
        
        def dijkstra(start, graph):
            dist = [INF] * n
            dist[start] = 0

            pq = [(0, start)] 
            while pq:
                cur_weight, u = heapq.heappop(pq)
                
                if cur_weight > dist[u]:
                    continue

                for v, w in graph[u]:
                    new_w = cur_weight + w
                    if dist[v] > new_w:
                        dist[v] = new_w
                        heapq.heappush(pq, (new_w, v))
            return dist

        dist1 = dijkstra(src1, graph)
        dist2 = dijkstra(src2, graph)
        print(dist1)
        print(dist2)
        dest_to_u = dijkstra(dest, reverse_graph)
        print(dest_to_u)
        best = INF
        for u in range(n):
            if dist1[u] == INF or dist2[u] == INF or dest_to_u[u] == INF:
                continue
            total = dist1[u] + dist2[u] + dest_to_u[u]
            best = min(total, best)
        return best if best < INF else -1

        
