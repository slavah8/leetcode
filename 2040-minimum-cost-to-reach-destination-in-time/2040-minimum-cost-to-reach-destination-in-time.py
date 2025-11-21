class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)

        # dp[u][t] min cost to reach node u at time t

        INF = 10 ** 10
        dp = [[INF] * (maxTime + 1) for _ in range(n)]
        graph = defaultdict(list)
        dp[0][0] = passingFees[0]

        pq = [(passingFees[0], 0, 0)] # (cost, u, time)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        while pq:
            cur_cost, u, cur_time = heapq.heappop(pq)

            if cur_time > maxTime:
                continue

            if u == n - 1:
                return cur_cost

            for v, t in graph[u]:
                time = t + cur_time
                cost = cur_cost + passingFees[v]
                if time <= maxTime and cost < dp[v][time]:
                    dp[v][time] = cost
                    heapq.heappush(pq, (cost, v, time))
        
        return -1
                     
