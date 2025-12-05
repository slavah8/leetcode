class Solution:

    def count(self, x, d):
        if x < 0:
            return 0
        
        
            
        s = str(x)
        L = len(s)
        target = d

        @lru_cache(None)
        def dfs(pos, tight, started):
            # returns (ways, total occurrences of target)
            if pos == L:
                return (1 if started else 0, 0)
            
            limit = int(s[pos]) if tight else 9
            total_ways = 0 # how many valid numbers can be formed from this position onward
            total_occ = 0 # among all those numbers, the total number of times digit d appears in the remaining positions

            # option 1: skip (leading zero)
            if not started:
                child_ways, child_occ = dfs(pos + 1, tight and 0 == limit, False)
                total_ways += child_ways
                total_occ += child_occ
            
            for dig in range(0, limit + 1):
                if not started and dig == 0:
                    continue
                
                next_tight = tight & (dig == limit)
                child_ways, child_occ = dfs(pos + 1, next_tight, True)

                total_ways += child_ways
                total_occ += child_occ

                if dig == target:
                    total_occ += child_ways
            
            return (total_ways, total_occ)

        _, total_occ = dfs(0, True, False)
        return total_occ




    def digitsCount(self, d: int, low: int, high: int) -> int:
        return self.count(high, d) - self.count(low - 1, d)
        