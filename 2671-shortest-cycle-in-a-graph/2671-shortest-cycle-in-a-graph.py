class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        INF = 10 ** 10
        ans = INF

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for start in range(n):
            queue = deque()
            dist = [-1] * n
            parent = [-1] * n
            dist[start] = 0
            queue.append(start)
            
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        queue.append(v)
                    elif parent[u] != v:
                        # non tree edge which means a cycle
                        length = dist[u] + dist[v] + 1
                        ans = min(ans, length)

        return ans if ans != INF else -1
                

