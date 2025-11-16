class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        print(degree)
        print(graph)
        queue = deque()
        for node in range(n):
            if degree[node] == 1:
                queue.append(node)
        
        in_cycle = [True] * n

        while queue:
            node = queue.popleft()
            in_cycle[node] = False
            for nei in graph[node]:
                degree[nei] -= 1
                if degree[nei] == 1:
                    queue.append(nei)
        
        print(degree)
        print(in_cycle)

        dist = [-1] * n
        for node in range(n):
            if in_cycle[node]:
                dist[node] = 0
                queue.append(node)

        
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if dist[nei] == -1:
                    dist[nei] = dist[node] + 1
                    queue.append(nei)
        
        return dist
