class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        summ = sum(ribbons)
        
        low = 1
        high = max(ribbons)

        def ribbons_count(length):
            count = 0
            for x in ribbons:
                count += math.floor(x / length)
            return count >= k



        while low < high:
            mid = (low + high + 1) // 2

            if ribbons_count(mid):
                low = mid
            else:
                high = mid - 1
        return low if ribbons_count(low) else 0
