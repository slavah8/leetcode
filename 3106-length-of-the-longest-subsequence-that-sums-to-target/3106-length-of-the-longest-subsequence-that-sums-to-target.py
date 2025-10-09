class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        

        # dp[i][s] = max length to make sum s using the first i numbers (nums[0..i-1]), or -inf if impossible

        INF = 10 ** 10
        N = len(nums)
        dp = [[-INF] * (target + 1) for _ in range(N + 1)]

        dp[0][0] = 0

        for i in range(1, N + 1):
            x = nums[i - 1]
            for s in range(target + 1):
                # skip 
                best = dp[i - 1][s]

                # take
                cand = -INF
                if s - x >= 0:
                    cand = 1 + dp[i - 1][s - x]
                if cand > best:
                    best = cand
                
                dp[i][s] = best
        ans = dp[N][target]
        return -1 if ans < 0 else ans



