class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        L = len(s)

        @lru_cache(None)
        def dfs(pos, tight, started, mask):
            if pos == L:
                return 1 if started else 0
            
            limit_digit = int(s[pos]) if tight else 9
            res = 0

            # Option 1 : still skip leading zeros
            if not started:
                res += dfs(pos + 1, tight and limit_digit == 0, False, mask)
            
            # Option 2: place a real digit
            for d in range(0, limit_digit + 1):
                if not started and d == 0:
                    continue
                
                if mask & (1 << d):
                    # digit already used -> skip
                    continue
                
                next_tight = tight and (d == limit_digit)
                next_mask = mask | (1 << d)
                res += dfs(pos + 1, next_tight, True, next_mask)
            
            return res

        count_no_repeat = dfs(0, True, False, 0)
        return n - count_no_repeat