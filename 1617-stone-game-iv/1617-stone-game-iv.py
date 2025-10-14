class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @lru_cache(maxsize= None)
        def win(stones):
            # squares 1 4 9 16 25 36
            r = isqrt(stones)
            for x in range(1, r + 1):
                t = stones - x * x
                if t == 0 or not win(t):
                    return True
                    
            return False
        
        return win(n)