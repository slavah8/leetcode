class Solution:
    def soupServings(self, n: int) -> float:
        
        if n >= 4800:
            return 1.0
        M = math.ceil(n / 25)
        @lru_cache(maxsize=None)
        def P(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            
            elif a > 0 and b <= 0:
                return 0.0
            
            elif a <= 0 and b > 0:
                return 1.0
        
            return 0.25 * (
                P(a - 4, b) +
                P(a - 3, b - 1) + 
                P(a - 2, b - 2) + 
                P(a - 1, b - 3)
            )
        return P(M, M)