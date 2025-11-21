class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        INF = 10 ** 10
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(start):
            dist1 = [INF] * (n + 1) # shortest
            dist1[start] = 0
            dist2 = [INF] * (n + 1) # second shortest

            queue = deque([(1, 0)]) # (node, steps)
            while queue:
                u, steps = queue.popleft()
                
                for v in graph[u]:
                    new_dist = steps + 1
                    if new_dist < dist1[v]:
                        dist2[v] = dist1[v]
                        dist1[v] = new_dist
                        queue.append((v, new_dist))
                    elif dist1[v] < new_dist < dist2[v]:
                        dist2[v] = new_dist
                        queue.append((v, new_dist))
                
            return dist1, dist2
        
        dist1, dist2 = bfs(1)
        print(dist1)
        print(dist2)
        def simulate(k):
            t = 0
            for _ in range(k):
                phase = t // change
                if phase % 2 == 1: # odd so it's red
                    t = (phase + 1) * change
                t += time
            return t

        return simulate(dist2[n])