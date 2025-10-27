class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        N1 = len(nums1)
        N2 = len(nums2)
        # cost[i][j] = nums1[i] ^ nums2[j]
        cost = [[0] * N2 for _ in range(N1)]
        INF = 10 ** 15

        for i in range(N1):
            for j in range(N2):
                cost[i][j] = nums1[i] ^ nums2[j]

        # dp(mask) : minimum XOR sum after assigning the mentors in mask to the first popcount(mask) positions of nums1.
        @lru_cache(None)
        def dp(mask):
            i = mask.bit_count() # next bit in nums1
            if i == N1: # all bits set in N1
                return 0

            best = INF

            for j in range(N2): # try all nums in nums2 for this num1
                if (mask >> j) & 1 == 1:
                    continue
                best = min(best, cost[i][j] + dp(mask | (1 << j)))
            return best
                
        
        return dp(0)
