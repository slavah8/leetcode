class Solution:

    def countDigitOne(self, n: int) -> int:

        s = str(n)
        L = len(s)

        # return (number of valid numbers, total occurrences of 1)
        @lru_cache(None)
        def dfs(pos, tight, started):
            
            if pos == L:
                return (1 if started else 0, 0) 
            
            limit = int(s[pos]) if tight else 9
            total_ways = 0 # total number of valid numbers 
            total_occ = 0 # total number of numbers with digit 1 appearing

            if not started:
                child_ways, child_occ = dfs(pos + 1, tight & (limit == 0), False)
                total_ways += child_ways
                total_occ += child_occ
            
            for d in range(0, limit + 1):
                if d == 0 and not started:
                    continue
                
                next_tight = tight & (d == limit)

                child_ways, child_occ = dfs(pos + 1, next_tight, True)
                total_ways += child_ways
                total_occ += child_occ

                if d == 1:
                    total_occ += child_ways

            return (total_ways, total_occ)
                
            

        
        _, occ = dfs(0, True, False)
        return occ
        
        