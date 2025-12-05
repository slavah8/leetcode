class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)
        L = len(s)

        same = {0, 1, 8}
        diff = {2, 5, 6, 9}
        bad = {3, 4, 7}

        @lru_cache(None)
        def dfs(pos, tight, hasDiff):
            if pos == L:
                return 1 if hasDiff else 0
            
            res = 0
            # if we are still tight with n then at this position we cannot exceed the digit in the n at this spot
            # so max digit we can place is int(s[pos])

            limit = int(s[pos]) if tight else 9
            for d in range(0, limit + 1):
                if d in bad:
                    continue

                next_tight = tight and (d == limit)
                next_hasDiff = hasDiff or (d in diff)
                res += dfs(pos + 1, next_tight, next_hasDiff)

            return res 

        

        return dfs(0, True, False)