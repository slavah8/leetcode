class Solution:
    def minInsertions(self, s: str) -> int:
        N = len(s)

        # dp[i][j] = minimum insertions to make the substring s[i..j] a palindrome
        dp = [[0] * N for _ in range(N)]

        for length in range(2, N + 1):
            for i in range(N - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    # insert at right end then (i + 1, j)
                    # insert at left end then (i, j - 1)
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
        print(dp)
        return dp[0][N - 1]