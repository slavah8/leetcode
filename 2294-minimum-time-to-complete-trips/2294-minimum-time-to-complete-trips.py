class Solution:
    def minimumTime(self, times: List[int], totalTrips: int) -> int:
        
        def num_trips(time):
            trips = 0
            for x in times:
                trips += math.floor(time / x)
            return trips >= totalTrips
        
        # binary search on minimum time to complete at least totalTrips
        low = 1
        high = 10 ** 20

        while low < high:
            mid = (low + high) // 2
            if num_trips(mid):
                high = mid
            else:
                low = mid + 1
        return low 