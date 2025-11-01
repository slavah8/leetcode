class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        n = len(points)
        INF = 10 ** 15
        def canonical_slope(dy, dx):
            if dx == 0:
                return (1, 0)
            if dy == 0:
                return (0, 1)
            
            g = gcd(dy, dx)
            dy = dy // g
            dx = dx // g

            if dx < 0:
                dx = -dx
                dy = -dy
            return (dy, dx)
        
        line_masks = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                base = canonical_slope(yj - yi, xj - xi)
                
                mask = 0
                for k in range(n):
                    if k == i:
                        mask |= (1 << k)
                        continue
                        
                    xk, yk = points[k]
                    s = canonical_slope(yk - yi, xk - xi)
                    if base == s:
                        mask |= (1 << k)
                line_masks.append(mask)
        
        for i in range(n):
            line_masks.append(1 << i) # covers point i
        
        line_masks = list(set(line_masks))

        FULL = (1 << n) - 1
        @lru_cache(None)
        def dp(mask):
            if mask == FULL:
                return 0
            
            # find first uncovered point
            idx = 0
            while (mask >> idx) & 1:
                idx += 1
            
            best = INF
            for m in line_masks:
                if (m >> idx) & 1:
                    new_mask = mask | m
                    best = min(best, 1 + dp(new_mask))
            return best

        return dp(0)
        

                    