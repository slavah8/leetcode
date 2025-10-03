class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        low = 1
        high = max(candies)

        def can_divide(c):
            piles = 0
            for x in candies:
                piles += math.floor(x / c)
            return piles >= k

        while low < high:
            mid = (low + high + 1) // 2

            if can_divide(mid):
                low = mid
            else:
                high = mid - 1
        return low if can_divide(low) else 0
