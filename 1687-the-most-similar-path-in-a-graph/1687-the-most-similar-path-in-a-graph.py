class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        
        graph = defaultdict(list)

        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        INF = 10 ** 10
        m = len(targetPath)

        # dp[t][c] = minimum edit distance for a path of length t+1
        # that ends at city c at position t
        dp = [[INF] * n for _ in range(m)]
        parent = [[-1] * n for _ in range(m)]

        # base case: we can start at any city
        for c in range(n):
            dp[0][c] = 0 if names[c] == targetPath[0] else 1
        
        print(dp)
        for t in range(1, m):
            for c in range(n):
                # We must come from some neighbor p of c at position t-1
                best_prev = INF
                best_city = -1
                for p in graph[c]:
                    if dp[t - 1][p] < best_prev:
                        best_prev = dp[t - 1][p]
                        best_city = p

                mismatch = 0 if names[c] == targetPath[t] else 1
                dp[t][c] = best_prev + mismatch
                parent[t][c] = best_city
        
        last_city = min(range(n), key = lambda c: dp[m - 1][c])
        path = [0] * m
        cur = last_city
        for t in range(m - 1, -1, -1):
            path[t] = cur
            cur = parent[t][cur] if t > 0 else -1
        return path

