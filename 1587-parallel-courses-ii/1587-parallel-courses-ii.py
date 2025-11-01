class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # build prereq mask for each course
        INF = 10 ** 9
        need = [0] * n
        for u, v in relations:
            need[v - 1] |= (1 << u - 1)
        
        full = (1 << n) - 1
        @lru_cache(None)
        def dp(mask):
            # mask over courses taken
            if mask == full:
                return 0
            
            # courses not taken yet
            remain = ~mask & full # 1s set for courses not taken yet


            avail = 0
            m = remain
            while m:
                # course index
                c = (m & -m).bit_length() - 1 # index of lowest set bit
                # course is takeable if all its prereqs are done and its bit is not set
                # check if need[c] is a subset of mask
                if (need[c] & mask) == need[c]:
                    avail |= (1 << c)
                # clears the lowest set bit of m (classic trick) so the loop moves on to the next set bit
                m &= (m - 1)

            cnt = avail.bit_count()
            # take as many courses as possible up to k
            if cnt <= k:
                return 1 + dp(mask | avail)
            
            # otherwise choose any subset <= k
            best = INF
            sub = avail
            while sub:
                if sub.bit_count() <= k:
                    best = min(best, 1 + dp(mask | sub))
                sub = (sub - 1) & avail
            return best
        return dp(0)
            




