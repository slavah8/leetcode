class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        
        rev_graph = defaultdict(list)
        max_W = 0
        for u, v, w in edges:
            rev_graph[v].append((u, w))
            if w > max_W:
                max_W = w
        

        def can(W):
            visited = [False] * n
            queue = deque([0])
            cnt = 1
            visited[0] = True
            while queue:
                u = queue.popleft()
                for v, w in rev_graph[u]:
                    if w <= W and not visited[v]:
                        cnt += 1
                        visited[v] = True
                        queue.append(v)
            
            return cnt == n
        
        low = 0
        high = max_W
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        
        return ans


            

