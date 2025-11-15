class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        nodes = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            nodes.add(u)
            nodes.add(v)

        
        for star, neighbors in graph.items():
            nodes.remove(star)
            if set(neighbors) == nodes:
                return star
            nodes.add(star)