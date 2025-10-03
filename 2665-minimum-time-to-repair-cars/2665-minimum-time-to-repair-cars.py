class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # r * n^2 = time
        # count^2 = time / r
        # count = sqrt(time / r)
        # total_time = sum
        # can repair all the cars in this time or less
        def can_repair(time):
            count = 0
            for r in ranks:
                count += math.isqrt(time // r)
            return count >= cars
        
        low = 0
        # fastest mechanic doing all the work
        high = min(ranks) * (cars ** 2)

        while low < high:
            mid = (low + high) // 2
            if can_repair(mid):
                high = mid
            else:
                low = mid + 1
        return low
                