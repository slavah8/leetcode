class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        
        # cost[u][d] = min cost to reach u using d discounts
        INF = 10 ** 10
        cost = [[INF] * (discounts + 1) for _ in range(n)]

        print(cost)
        graph = defaultdict(list)
        for u, v, w in highways:
            graph[u].append((v, w))
            graph[v].append((u, w))

        pq = [(0, 0, 0)] # (cost, node, discounts_used)

        while pq:
            c, u, used = heapq.heappop(pq)
            if u == n - 1:
                return c
            for v, w in graph[u]:
                new_cost = c + w
                discounted = w // 2
                discounted_cost = c + discounted
                if cost[v][used] > new_cost:
                    cost[v][used] = new_cost
                    heapq.heappush(pq, (new_cost, v, used))
                if used + 1 <= discounts and cost[v][used + 1] > discounted_cost:
                    cost[v][used + 1] = discounted_cost
                    heapq.heappush(pq, (discounted_cost, v, used + 1))
        return -1
            
