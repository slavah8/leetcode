class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        MOD = 10 ** 9 + 7

        # number of ways to get target with k faces

        # dp[curr_sum][dice_remaining]

        @lru_cache(None)
        def dp(curr_sum, dice_remaining):
            
            if dice_remaining == 0 and curr_sum == target:
                return 1
            
            if dice_remaining == 0 and curr_sum < target:
                return 0
            
            if curr_sum > target:
                return 0
            
            ways = 0

            for face in range(1, k + 1):
                ways += dp(curr_sum + face, dice_remaining - 1)
            
            return ways % MOD
            

    

        return dp(0, n) % MOD

        

