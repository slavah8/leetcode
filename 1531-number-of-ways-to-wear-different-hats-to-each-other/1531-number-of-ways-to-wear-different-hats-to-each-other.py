class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        MOD = 10 ** 9 + 7

        want = [[] for _ in range(41)] # Build hat -> list of people who like it
        for person, lst in enumerate(hats):
            for h in lst:
                want[h].append(person)
        
        FULL = (1 << n) - 1
        # dp(h, mask) = number of ways to finish assigning hats 
        # considering hats h..40 when the set of already assigned people is mask.
        @lru_cache(None)
        def dp(mask, h):
            if mask == FULL:
                return 1

            if h > 40:
                return 0
            
            # option 1: skip hat h
            total = dp(mask, h + 1)
            
            # assign to a liker
            for p in want[h]:
                if ((mask >> p) & 1) == 0: # unassigned
                    new_mask = mask | (1 << p)
                    total = (total + dp(new_mask, h + 1)) % MOD
            return total % MOD
        return dp(0, 1)


