class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        fuel = 0
        def dfs(u, parent):
            nonlocal fuel
            people = 1
            for v in graph[u]:
                if v == parent:
                    continue
                subtree = dfs(v, u)
                people += subtree
                fuel += math.ceil(subtree / seats)
            return people
                
            
        dfs(0, -1)
        return fuel
