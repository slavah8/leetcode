class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        
        s = str(n)
        L = len(s)

        @lru_cache(None)
        def dfs(pos, tight, started, mask):
            if pos == L:
                return 1 if started else 0

            limit_digit = int(s[pos]) if tight else 9
            res = 0
            if not started:
                res += dfs(pos + 1, tight & (limit_digit == 0), False, mask)
                
            for d in range(0, limit_digit + 1):
                if d == 0 and not started:
                    continue
                
                if mask & (1 << d):
                    continue
                
                next_tight = tight & (d == limit_digit)
                next_mask = mask | (1 << d)
                res += dfs(pos + 1, next_tight, True, next_mask)

            return res

            
        return dfs(0, True, False, 0)