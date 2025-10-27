class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        m = n // k # # of subsets
        count = Counter(nums)
        INF = 10 ** 15

        if any(c > k for c in count.values()):
            return -1
        

        # list(combinations(range(4), 2))
        # [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
        valid_by_first = [[] for _ in range(n)]
        for comb in combinations(range(n), m):
            vals = [nums[i] for i in comb]
            if len(set(vals)) < m:
                continue
            cost = max(vals) - min(vals)
            mask = 0
            for i in comb:
                mask |= 1 << i
            first = min(comb)
            valid_by_first[first].append((mask, cost))
        
        FULL = (1 << n) - 1

        # mask : what indices have been placed
        # dp(mask) = minimum total incompatibility to fill exactly the indices in mask with disjoint valid groups of size m = n/k
        @lru_cache(None)
        def dp(mask):
            if mask == FULL:
                return 0
            
            # find first unused index
            for i in range(n):
                if (mask & (1 << i)) == 0:
                    first_unused = i
                    break
                    
            best = INF
            for gmask, cost in valid_by_first[first_unused]:
                if gmask & mask == 0: # disjoint
                    best = min(best, cost + dp(mask | gmask))
            return best
        
        return dp(0)

