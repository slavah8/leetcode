class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        N = len(values)
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))

        print(graph)
        best = 0
        visited = [0] * N
        

        def dfs(u, t, score): # cur node time and score
            nonlocal best
            if u == 0:
                if score > best:
                    best = score
            
            for v, w in graph[u]:
                nt = t + w
                if nt > maxTime:
                    continue
                first_time = (visited[v] == 0)
                visited[v] += 1
                dfs(v, nt, score + (values[v] if first_time else 0))
                visited[v] -= 1
        visited[0] = 1
        dfs(0, 0, values[0])
        return best

