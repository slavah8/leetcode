class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        
        n = len(nums)
        INF = 10 ** 10
        # dp[t] = minimum number of valid subarrays to cover the prefix nums[0..t-1] (first t elements).
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue
            
            for j in range(i, n):
                if math.gcd(nums[i], nums[j]) > 1:
                    dp[j + 1] = min(dp[j + 1], dp[i] + 1)
        
        return -1 if dp[n] >= INF else dp[n]

