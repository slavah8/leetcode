class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        
        connected = [[False] * (n + 1) for _ in range(n + 1)]

        deg = [0] * (n + 1)
        for u, v in edges:
            connected[u][v] = True
            connected[v][u] = True
            deg[u] += 1
            deg[v] += 1
        
        INF = 10 ** 10


        min_degree = INF
        for u in range(1, n + 1):
            for v in range(u + 1, n + 1):
                if not connected[u][v]:
                    continue
                
                for w in range(v + 1, n + 1):
                    if connected[w][u] and connected[w][v]: # valid trio
                        
                        degree = deg[u] + deg[v] + deg[w] - 6
                        if degree < min_degree:
                            min_degree = degree
                        
        return min_degree if min_degree < INF else -1
