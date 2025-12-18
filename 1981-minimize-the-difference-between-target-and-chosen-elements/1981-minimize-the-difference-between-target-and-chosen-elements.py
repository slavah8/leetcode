class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        
        rows = len(mat)
        cols = len(mat[0])
        max_sum = 70 * rows
        # dp defined as dp[r][s]
        # True if it’s possible to choose one element from each of the first r rows 
        # such that the total sum is exactly s.

        dp = [[False] * (max_sum + 1) for _ in range(rows + 1)]

        dp[0][0] = True

        for r in range(1, rows + 1):
            row = mat[r - 1]
            for s in range(max_sum + 1):
                if dp[r - 1][s]:
                    for v in row:
                        dp[r][s + v] = True
        
        INF = 10 ** 10
        ans = INF
        for s in range(max_sum + 1):
            if dp[rows][s]:
                ans = min(ans, abs(target - s))
        return ans

