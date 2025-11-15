class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        color = [0] * (n + 1) # possible colors are 1 2 3 4. 0 if not assigned yet
        graph = defaultdict(list)

        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        

        for node in range(1, n + 1):
            
            # collect colors used in neighbors
            used = set()
            for nei in graph[node]:
                used.add(color[nei])
            print(used)
            for c in range(1, 5):
                if c not in used:
                    color[node] = c
        return color[1:]
                