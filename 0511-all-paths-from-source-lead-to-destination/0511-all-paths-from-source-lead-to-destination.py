class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        

        # check for loops
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            
        
        # 0 = unvisited, 1 = visiting (on recursion stack), 2 = done & valid
        state = [0] * n
        def dfs(node):
            if state[node] == 1:
                return False
            
            if state[node] == 2:
                return True
            
            if not graph[node]: # if the node has no outgoing edges, then it has to be the destination
                return node == destination

            # mark as visiting    
            state[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
                    
            state[node] = 2
            return True
                
        return dfs(source)
        
        