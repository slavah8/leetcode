from typing import List

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        # base: single element takes 1 move
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # option A: remove arr[i] alone, then the rest
                best = 1 + dp[i + 1][j]

                # option C: pair arr[i] with some equal arr[t]
                for t in range(i + 1, j + 1):
                    if arr[t] == arr[i]:
                        right = dp[t + 1][j] if t + 1 <= j else 0
                        if t == i + 1:
                            # adjacent equal → 1 move for the pair, then solve the right
                            best = min(best, 1 + right)
                        else:
                            # clear middle, then i merges with t in the same final move
                            left = dp[i + 1][t - 1]
                            best = min(best, left + right)

                dp[i][j] = best

        return dp[0][n - 1]

