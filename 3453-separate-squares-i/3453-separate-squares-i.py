class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        INF = 10 ** 10
        total = 0
        low = INF
        high = -INF

        for x, y, l in squares:
            total += l * l
            low = min(low, y)
            high = max(high, y + l)

        target = total / 2
        
        def area_below(Y):
            res = 0.0
            for x, y, l in squares:
                h = Y - y
                if h <= 0:
                    continue
                
                if h >= l:
                    res += l * l
                else:
                    res += h * l
            
            return res
                
                


        # Binary search for minimum Y such that area_below(Y) >= target
        left, right = float(low), float(high)

        for _ in range(80):
            mid = (left + right) / 2.0
            if area_below(mid) >= target:
                # move line down
                right = mid
            else:
                left = mid
        return right
