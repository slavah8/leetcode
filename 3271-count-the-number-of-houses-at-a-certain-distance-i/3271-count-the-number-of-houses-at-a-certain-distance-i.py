class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        graph = defaultdict(list)
        for i in range(1, n + 1):
            if i < n:
                graph[i].append(i + 1)
                graph[i + 1].append(i)
        
        graph[x].append(y)
        graph[y].append(x)
        
        # we want to count how many pairs are reachable with k edges
        def bfs(start, k):
            dist = [-1] * (n + 1)
            dist[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if dist[nei] == -1:
                        dist[nei] = dist[node] + 1
                        if dist[nei] <= k:
                            queue.append(nei)
            
            return start, dist

        result = [0] * (n + 1)
        for k in range(1, n + 1):
            count = 0
            for node in range(1, n + 1):
                # start bfs from this node and count how many houses are distance k
                node, dist = bfs(node, k)
                for d in dist:
                    if d == k:
                        count += 1
            result[k] = count
        return result[1:]
                
            

