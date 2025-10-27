class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        
        nums.sort()
        N = len(nums)

        def is_square(x):
            if isqrt(x) * isqrt(x) == x:
                return True
            else:
                return False

        ok = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                x = nums[i] + nums[j]
                if i != j and is_square(x):
                    ok[i][j] = True
        
        @lru_cache(None)
        def dp(used_mask, last):
            if used_mask == (1 << N) - 1:
                return 1

            total = 0

            for j in range(N): # j : indices
                if (used_mask >> j) & 1: # already used num
                    continue
                
                if j > 0 and nums[j - 1] == nums[j] and ((used_mask >> (j-1)) & 1) == 0:
                    continue
                if ok[last][j]:
                    total += dp(used_mask | (1 << j), j)
            return total
                
        
        ans = 0
        for i in range(N):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            ans += dp(1 << i, i)
        return ans


        