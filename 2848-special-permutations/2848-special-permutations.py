class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # mask is an n-bit set of used indices
        N = len(nums)

        can = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i != j:
                    a, b = nums[i], nums[j]
                    can[i][j] = (a % b == 0) or (b % a == 0)
        
        @lru_cache(None)
        def dp(mask, last):
            # mask (n-bit): which indices are already used.
            # last (0..n-1): the index of the last picked number in the current partial sequence
            if mask == (1 << N) - 1: # every index is used
                return 1
            
            total = 0
            # unused candidates that can follow "last"
            for j in range(N):
                if (mask >> j) & 1 == 1:
                    continue # already used
                if can[last][j]:
                    total = (total + dp(mask | (1 << j), j)) % MOD
            return total % MOD
                
        ans = 0
        for i in range(N):
            # dp(1 << i, i) means: start a path that uses only index i so far, and ends at i.
            ans = (ans + dp(1 << i, i)) % MOD
        return ans
        