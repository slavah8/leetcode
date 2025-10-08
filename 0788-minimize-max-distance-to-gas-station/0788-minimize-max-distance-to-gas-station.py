class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        
        N = len(stations)
        gaps = []
        for i in range(N - 1):
            gaps.append(stations[i + 1] - stations[i])
        
        # can we add k gas stations so that each adjacent distance is at most D?
        def possible(D):
            total = 0
            eps = 1e-12
            for L in gaps:
                # m = the number of new gas stations you place inside a single gap
                m = math.ceil(L / (D + eps)) - 1
                if m < 0:
                    m = 0
                total += m
            return total
        
        low = 0.0
        high = max(gaps) if gaps else 0.0

        for _ in range(60):
            mid = (low + high) / 2.0
            if possible(mid) <= k:
                high = mid
            else:
                low = mid
        return high
            