class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        nodes = [-1] * (n) # return this

        print(graph)
        def bfs(start, graph, n):
            dist = [-1] * n
            queue = deque([start])
            dist[start] = 0
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if dist[nei] == -1:
                        dist[nei] = dist[node] + 1
                        queue.append(nei)
            
            far = max(range(n), key = lambda i: dist[i]) #  furthest node from start
            return far, dist

        # find furthest node from 0 - > u
        u, dist = bfs(0, graph, n)
        print(u)
        print(dist)

        # find furthest node v from u and all distances from u
        v, dist_u = bfs(u, graph, n)
        print(v)
        print(dist_u)
        # find all distances from v 
        _, dist_v = bfs(v, graph, n)


        # now last marked node is the one with either furthest distance from u or v
        for i in range(n):
            if dist_v[i] > dist_u[i]:
                nodes[i] = v
            else:
                nodes[i] = u
        return nodes



         