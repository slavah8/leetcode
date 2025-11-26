class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        INF = 10 ** 10
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)
        
        print(graph)
        def bfs(start):
            dist = [INF] * n
            dist[start] = 0
            queue = deque([(start, 0)])
            while queue:
                u, d = queue.popleft()
                if u == n - 1:
                    return d
                for v in graph[u]:
                    if dist[v] == INF:
                        dist[v] = 1 + d
                        queue.append((v, 1 + d))

        answer = []
        for q in queries:
            u, v = q
            graph[u].append(v)
            shortest_dist = bfs(0)
            answer.append(shortest_dist)
        return answer