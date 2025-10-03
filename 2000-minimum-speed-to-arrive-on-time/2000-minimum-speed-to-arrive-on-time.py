class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        N = len(dist)
        if hour < N - 1:
            return -1

        low = 1
        high = 10 ** 7
        def feasible(speed):
            total = 0
            for i in range(N - 1):
                total += math.ceil(dist[i] / speed)
                if total > hour:
                    return False
            total += dist[-1] / speed
            if total <= hour:
                return True


        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low if feasible(low) else -1