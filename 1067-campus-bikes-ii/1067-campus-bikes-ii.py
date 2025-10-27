class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        N, M = len(workers), len(bikes)
        INF = 10 ** 15

        # # Precompute Manhattan distances dist[i][j] between worker i and bike j
        dist = [[0] * M for _ in range(N)]
        for i in range(N):
            x1, y1 = workers[i]
            for j in range(M):
                x2, y2 = bikes[j]
                dist[i][j] = abs(x1 - x2) + abs(y1 - y2)
        print(dist)

        # dp(mask) = minimum total distance after assigning bikes in mask to the first popcount(mask) workers.
        def dp(mask):
            i = mask.bit_count() # next worker index (0 .. n)
            if i == N:
                return 0 # all workers assigned
            best = INF
            for j in range(M):
                # check if bike j has been assigned
                if (mask >> j) & 1 == 1:
                    continue
                best = min(best, dist[i][j] + dp(mask | (1 << j)))
            return best
            

        
        return dp(0)
