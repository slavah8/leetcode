class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        INF = 10 ** 10
        # dp[u][used] defined as shortest path to u hopping over used edges
        dp = [[INF] * (k + 1) for _ in range(n)]
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        pq = [(0, s, 0)] # (weight, node, used)
        dp[s][0] = 0
        while pq:
            cur_weight, u, used = heapq.heappop(pq)
            if u == d:
                return cur_weight

            for v, w in graph[u]:
                new_weight = cur_weight + w
                
                if new_weight < dp[v][used]:
                    dp[v][used] = new_weight
                    heapq.heappush(pq, (new_weight, v, used))
                if used + 1 <= k and cur_weight < dp[v][used + 1]:
                    dp[v][used + 1] = cur_weight
                    heapq.heappush(pq, (cur_weight, v, used + 1))
            

        