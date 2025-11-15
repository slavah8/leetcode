class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list) # node : prerequisites
        indegree = [0] * n
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        
        print(indegree)
    
        print(graph)
        # prereq[v][u] = True if u is a (direct or indirect) prerequisite of v
        prereq = [[False] * n for _ in range(n)]


        
        
        queue = deque()
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)
        
        while queue:
            u = queue.popleft()

            for v in graph[u]:
                # direct prerequisite 
                prereq[v][u] = True
                for x in range(n):
                    if prereq[u][x] == True:
                        prereq[v][x] = True

                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
                
        print(prereq)
        result = []
        for u, v in queries:
            result.append(prereq[v][u])
        return result

            

        
        