class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        num = (10 ** n) - 1

        s = str(num)
        L = len(s)

        
        @lru_cache(None)
        def dfs(pos, tight, started, mask):
            if pos == L:
                return 1 if started else 0
            
            limit_digit = int(s[pos]) if tight else 9

            res = 0
            if not started:
                res += dfs(pos + 1, tight and limit_digit == 0, False, mask)
            
            # option 2 place a digit here
            for d in range(0, limit_digit + 1):
                if not started and d == 0:
                    continue
                
                if mask & (1 << d):
                    continue

                next_tight = tight and (d == limit_digit)
                next_mask = mask | (1 << d)
                res += dfs(pos + 1, next_tight, True, next_mask)
            return res


        
        return dfs(0, True, False, 0) + 1