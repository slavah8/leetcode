class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        sys.setrecursionlimit(2_000_000)
        INF = 10 ** 10
        n = len(obstacles) - 1
       
        @lru_cache(None)
        def dp(point, lane):
            
            if obstacles[point] == lane:
                return INF
            if point == n:
                return 0
            
            if obstacles[point + 1] != lane:
                return dp(point + 1, lane)
            
            # try going sideways
            best = INF
            for n_lane in (1, 2, 3):
                if n_lane == lane:
                    continue
                
                if obstacles[point] != n_lane:
                    best = min(best, 1 + dp(point, n_lane))
            return best
        

        return dp(0, 2)

