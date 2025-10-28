class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        # find as many points with same slope as possible
        
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
        
        ans = 1
        n = len(points)
        for i in range(n):
            # pick starting anchor
            counts = defaultdict(int)
            x1, y1 = points[i]
            local_max = 0
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                slope = canonical_slope(dy, dx)
                counts[slope] += 1
                if counts[slope] > local_max:
                    local_max = counts[slope]
            ans = max(ans, local_max + 1)
        return ans
