class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        
        m = len(nums)
        # pre compute gcd for every pair
        G = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                g = gcd(nums[i], nums[j])
                G[i][j] = g
                G[j][i] = g

        @lru_cache(None)
        def dp(mask):
            used = mask.bit_count() # how many numbers are already taken from nums
    
            if used == m:
                return 0
            i = used // 2 + 1

            # This finds the first unused index u
            unused = [i for i in range(m) if ((mask >> i) & 1) == 0]
            
            best = 0
            # try 
            for a in range(len(unused)):
                u = unused[a]
                for b in range(a + 1, len(unused)):
                    v = unused[b]
                    new_mask = mask | (1 << u) | (1 << v)
                    cand = dp(new_mask) + (i * G[u][v])
                    if cand > best:
                        best = cand
            return best


        return dp(0)