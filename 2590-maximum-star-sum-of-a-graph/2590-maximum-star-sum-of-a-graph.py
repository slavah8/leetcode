class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append((-vals[v], v))
            graph[v].append((-vals[u], u))
        
        
        for node, neighbors in graph.items():
            heapify(neighbors)
        n = len(vals)
        print(graph)
        INF = 10 ** 10
        best = -INF
        for node in range(n):
            cand = vals[node]
            best = max(best, cand)

        for node, neighbors in graph.items():
            cand = vals[node]
            for _ in range(k):
                if not neighbors:
                    break
                neg_val, node = heapq.heappop(neighbors)
                val = -neg_val
                if val <= 0:
                    break
                cand += val
                    
            best = max(best, cand)
        return best




