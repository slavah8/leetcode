class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        answer = [-1] * n
        for u, v in redEdges:
            graph[u].append((v, 0)) # 0 for red
        
        for u, v in blueEdges:
            graph[u].append((v, 1)) # 1 for blue

        print(graph)
        queue = deque([(0, -1, 0)]) # (node, color, distance)
        answer[0] = 0
        visited = [[False] * n for _ in range(2)]
        
        while queue:
            print(queue)
            u, curr_color, distance = queue.popleft()
            visited[curr_color][u] = True
            
            for v, color in graph[u]:
                if curr_color == color or visited[color][v]:
                    continue
                if answer[v] == -1:
                    answer[v] = distance + 1
                queue.append((v, color, distance + 1))
        
        return answer

        

