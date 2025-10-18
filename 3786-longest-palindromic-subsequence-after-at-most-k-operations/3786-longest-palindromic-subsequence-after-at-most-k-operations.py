class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        
        N = len(s)
        A = [ord(char) - 97 for char in s]

        # ring distance : min ops to make them equal
        def dist(a, b):
            d = abs(a - b)
            return d if d <= 13 else 26 - d
        
        # dp[i][j][b] = max LPS length in s[i..j] using at most b operations

        dp = [[[0] * (k + 1) for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for b in range(k + 1):
                dp[i][i][b] = 1
        
        for length in range(2, N + 1):
            for i in range(N - length + 1):
                j = i + length - 1
                cij = dist(A[i], A[j])

                for b in range(0, k + 1):
                    # option 1: skip left or skip right
                    best = dp[i + 1][j][b] if i + 1 <= j else 0
                    if i <= j - 1:
                        if dp[i][j - 1][b] > best:
                            best = dp[i][j - 1][b]
                    
                    # option 2: pair ends if we can afford the cost
                    if cij <= b:
                        inside = 0 if i + 1 > j - 1 else dp[i + 1][j - 1][b - cij]
                        cand = 2 + inside
                        if cand > best:
                            best = cand
                    
                    dp[i][j][b] = best
        return dp[0][N - 1][k]