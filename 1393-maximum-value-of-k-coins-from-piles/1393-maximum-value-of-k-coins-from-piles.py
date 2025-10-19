class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        
        N = len(piles)
        # prefix[i][t] = sum of top t coins from pile i (0-based pile index)
        prefix = []
        for pile in piles:
            pre = [0]
            s = 0
            for idx, coins in enumerate(pile, 1):
                if idx > k:
                    break
                s += coins
                pre.append(s)
            prefix.append(pre)

        # dp[i][x] = max value using first i piles (piles 0..i-1) taking exactly x coins
        INF = 10 ** 15
        dp = [[-INF] * (k + 1) for _ in range(N + 1)]

        dp[0][0] = 0
        for i in range(1, N + 1):
            m = len(prefix[i - 1]) - 1
            for x in range(0, k + 1):

                best = dp[i][x] # start -INF
                lim = min(m, x)
                for t in range(0, lim + 1): # taking t coins from current pile
                    prev = dp[i - 1][x - t] # means we take x - t from the first i - 1 piles
                    if prev == -INF:
                        continue
                    cand = prev + prefix[i - 1][t]
                    if cand > best:
                        best = cand
                dp[i][x] = best
        return dp[N][k]


        