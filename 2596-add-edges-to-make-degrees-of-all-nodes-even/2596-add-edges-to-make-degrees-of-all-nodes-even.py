class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        deg = [0] * (n + 1)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            deg[u] += 1
            deg[v] += 1
        
        odd = [i for i in range(1, n + 1) if deg[i] % 2 == 1]
        k = len(odd)

        if k == 0:
            return True
        
        if k == 2:
            a, b = odd
            
            if a not in graph[b]:
                return True # just connect these 2 if they arent already connected
            
            for x in range(1, n + 1):
                if x != a and x != b:
                    if x not in graph[a] and x not in graph[b]:
                        return True
            return False
        

        def can_pair(a, b, c, d):
            if a not in graph[b] and c not in graph[d]:
                return True
            else:
                return False
        if k == 4:
            a, b, c, d = odd

            if can_pair(a,b,c,d):
                return True
            
            if can_pair(a,c,b,d):
                return True
            
            if can_pair(a,d,b,c):
                return True
            
            return False

        return False