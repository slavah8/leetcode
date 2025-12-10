class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        graph = defaultdict(list)

        for u, v in paths:
            graph[u].append(v)
            graph[v]
        
        print(graph)

        for city, destinations in graph.items():
            if len(destinations) == 0:
                return city
        
        