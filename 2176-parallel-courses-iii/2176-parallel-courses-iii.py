class Solution:
    def minimumTime(self, N: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * (N + 1)

        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1
        
        queue = collections.deque()
        finish = [0] * (N + 1) # earliest finish time
        for i in range(1, N + 1):
            if indegree[i] == 0:
                queue.append(i)
                finish[i] = time[i - 1]
        
        ans = 0
        while queue:
            u = queue.popleft()
            ans = max(ans, finish[u])
            for v in graph[u]:
                finish[v] = max(finish[v], finish[u] + time[v - 1])
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return ans


