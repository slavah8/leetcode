class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        INF = 10 ** 10
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        

        def dijkstra(start):
            dist = [INF] * (n + 1) # cost to buy apple from node start and returning
            dist[start] = 0

            pq = [(0, start)] # (dist, node
            min_cost = appleCost[start - 1]
            end_node = start
            while pq:
                cur_dist, u = heapq.heappop(pq)
                back = cur_dist * k
                total_dist = cur_dist + back
                cand = appleCost[u - 1] + total_dist
                if cand < min_cost:
                    min_cost = cand
                    end_node = u
                
                for v, w in graph[u]:
                    new_dist = cur_dist + w
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        heapq.heappush(pq, (new_dist, v))
        
            return min_cost


        answer = []
        for u in range(1, n + 1):
            cost = dijkstra(u)
            answer.append(cost)
        return answer
