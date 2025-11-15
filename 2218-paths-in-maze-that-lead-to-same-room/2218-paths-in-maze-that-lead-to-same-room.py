class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        graph = defaultdict(list)
        adj_set = [set() for _ in range(n + 1)]
        for u, v in corridors:
            graph[u].append(v)
            graph[v].append(u)
            adj_set[u].add(v)
            adj_set[v].add(u)

        confusion = 0
        print(graph)
        for i in range(1, n + 1):
            neighbors = [u for u in graph[i] if u > i]
            m = len(neighbors)

            for idx in range(m):
                u = neighbors[idx]
                for j in range(idx + 1, m):
                    v = neighbors[j]
                    if v in adj_set[u]:
                        confusion += 1
        
        return confusion



        

        

