class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        people = k + 1
        n = len(sweetness)

        # can we make at least k + 1 pieces each with sum >= X?
        def can(X):
            curr_sum = 0
            pieces = 0
            for x in sweetness:
                curr_sum += x
                if curr_sum >= X:
                    pieces += 1
                    curr_sum = 0
                    
            return pieces >= people

        S = sum(sweetness)
        lo, hi = 0, S // (k + 1)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
