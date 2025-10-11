class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        # dp[i][j] defined as the difference in score from stones[i:j]
        # relation: dp[i][j] = max()
        N = len(stones)
        dp = [[0] * N for _ in range(N)]
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + stones[i]

        def S(l, r):
            return prefix[r + 1] - prefix[l]

        for length in range(2, N + 1):
            for i in range(N - length + 1):
                j = i + length - 1
                take_left = S(i + 1, j)
                take_right = S(i, j - 1)
                dp[i][j] = max(take_left - dp[i + 1][j], take_right - dp[i][j - 1])
        return dp[0][N - 1]
