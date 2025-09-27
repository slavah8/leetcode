class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        indegree = [0] * (N + 1)
        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1
        
        print(indegree)
        print(graph)
        queue = collections.deque()
        for i in range(1, N + 1):
            if indegree[i] == 0:
                queue.append(i)
        
        print(queue)
        semesters = 0
        topological_order = []
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                topological_order.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
            semesters += 1

        if len(topological_order) == N:
            return semesters
        else:
            return -1
            



        
